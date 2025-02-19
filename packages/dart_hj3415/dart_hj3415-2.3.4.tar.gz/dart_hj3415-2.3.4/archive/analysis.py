import os
import pickle
import datetime
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from util_hj3415 import noti, utils
from eval_hj3415 import report, score
from krx_hj3415 import krx
from db_hj3415 import mongo2, dbpath
from . import subjects
from . import data
from .opendart import Dart, DartInfo

import logging
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s: [%(name)s] %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.INFO)


class Pickle:
    """분석하고 노티한 공시번호를 피클로 저장하는 클래스

    Attributes:
        contents (data.NotiAndAnal): 분석하고 노티한 공시리스트

    """
    FILENAME = 'notiNanal.pickle'
    FULL_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), FILENAME)

    def __init__(self):
        """
        클래스를 생성하면 self.load() 함수를 호출하여 self.contents 를 채워준다.
        """
        self.contents = data.NotiAndAnal()
        is_load_success = self.load()
        if not is_load_success:
            self.load()

    def save(self):
        """
        self.contents 를 피클로 저장한다.
        """
        if not utils.isYmd(self.contents.date):
            raise Exception(f"Invalid date - {self.contents.date}(YYYYMMDD)")
        else:
            logger.debug(f'Save to pickle : {self.contents}')
            with open(self.FULL_PATH, "wb") as fw:
                pickle.dump(self.contents, fw)

    def init(self, date: str):
        """
        피클데이터를 date 날짜의 빈딕셔너리로 초기화한다.
        """
        if not utils.isYmd(date):
            raise Exception(f"Invalid date - {date}(YYYYMMDD)")
        else:
            self.contents.date = date
            self.contents.analysed = []
            self.contents.notified = []
            logger.debug(f'init {self.FULL_PATH}')
            with open(self.FULL_PATH, "wb") as fw:
                pickle.dump(self.contents, fw)

    def load(self) -> bool:
        """
        피클 데이터를 불러들여 self.contents 에 저장한다.\n
        << self.contents >>\n
        {'date': '20210309', 'notified': ['20210708900096',..... ], 'analysed': ['20210708800312',..... ]}

        Returns:
            bool: 정상적인 로딩이면 True, 에러가 발생했으면 False(이 경우 한번 더 load 함수를 호출해야함.)
        """
        try:
            with open(self.FULL_PATH, "rb") as fr:
                obj = pickle.load(fr)
                logger.debug(f'Load from pickle : {obj}')
                self.contents = obj
            return True
        except (EOFError, FileNotFoundError) as e:
            logger.error(e)
            with open(self.FULL_PATH, "wb") as fw:
                empty_contents = data.NotiAndAnal()
                empty_contents.date = datetime.datetime.today().strftime('%Y%m%d')
                empty_contents.analysed = []
                empty_contents.notified = []
                pickle.dump(empty_contents, fw)
            return False


pretested_subject = ('주식분할결정', '주식병합결정', '주식등의대량보유상황보고서', '자기주식처분결정', '공개매수신고서',
                     '전환사채권발행결정', '신주인수권부사채권발행결정', '교환사채권발행결정', '만기전사채취득',
                     '신주인수권행사', '소송등의', '주식배당결정', '주주총회소집결의', '회사합병결정', '회사분할결정')
available_subject = ()
enabled_subject = ('공급계약체결', '무상증자결정', '자기주식취득결정', '주식등의대량보유상황보고서', '특정증권등소유상황보고서',
                   '주식소각결정', '현물배당결정', '자산재평가실시결정', '유상증자결정', '매출액또는손익')


class AnalyseOneSubject:
    def __init__(self, client, driver, edate: str, subject: str, pkl: Pickle):
        # edate와 subject 형식 여부 확인
        if not utils.isYmd(edate):
            raise Exception(f"Invalid date - {edate}(YYYYMMDD)")
        if subject not in enabled_subject:
            raise Exception(f'{subject} is not available.')
        self.client = client
        self.driver = driver
        self.subject = subject
        self.dartinfo_list = Dart(self.client).make_dartinfos(edate=edate, title=subject)
        self.pickle = pkl

    def pre_ansys_test(self, dartinfo: DartInfo) -> bool:
        """
        1. 코드가 등록되지 않은 종목
        2. 이미 이전에 분석된 공시
        3. 이미 이전에 노티한 공시
        4. 스팩주
        => False 를 리턴한다.
        """
        if dartinfo.code not in krx.get_codes():
            # 아직 코드가 krx에 없는 경우는 넘어간다.
            print(f"\t{dartinfo.code} {dartinfo.name}is not registered in corp db yet..")
            time.sleep(.5)
            self.pickle.contents.analysed.append(dartinfo.rno)
            return False
        elif dartinfo.rno in self.pickle.contents.analysed:
            # 이미 분석된 경우는 넘어간다.
            print(f"\t<{dartinfo.rno}> already analysed")
            time.sleep(.5)
            return False
        elif dartinfo.rno in self.pickle.contents.notified:
            # 이미 노티된 경우는 넘어간다.
            print(f"\t<{dartinfo.rno}> already notified")
            time.sleep(.5)
            return False
        elif '스팩' in dartinfo.name:
            # 스팩 주식은 넘어간다.
            # 따로 매일 2000원 이하를 찾는 코드가 있다.
            print(f"\t<{dartinfo.name}> is a 스팩, so we will skipping...")
            time.sleep(.5)
            return False
        else:
            return True

    @staticmethod
    def is_trading_halt(code: str, driver: WebDriver) -> bool:
        """
        거래정지 종목인지 확인하고 거래 정지면 True 를 반환한다.
        불필요하게 여러번 드라이버를 생성하지 않기 위해 인자로 받아온다.
        """
        driver.get(f'https://m.stock.naver.com/index.html#/domestic/stock/{code}/total')
        time.sleep(1)
        try:
            element = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div[2]/strong')
            logger.debug(element.text)
            if '거래정지' in element.text:
                return True
            else:
                return False
        except NoSuchElementException:
            return False

    def notify_and_write_record(self, dartinfo: DartInfo, cls: subjects.DartSubject):
        """
        노티할만한 데이터를 텔레그램 노티하고 데이터베이스에 기록을 남긴다.
        """
        # 텔레그램으로 노티한다.
        print(f"We caught the important report..{dartinfo.rno}")
        noti.telegram_to(botname='dart', text=str(cls))
        noti.telegram_to(botname='eval', text=report.for_telegram(self.client, dartinfo.code))

        # 데이터베이스에 기록한다.
        noti_data = {'code': dartinfo.code,
                     'rcept_no': dartinfo.rno,
                     'rcept_dt': dartinfo.rdt,
                     'report_nm': dartinfo.rtitle,
                     'point': cls.score.point,
                     'text': cls.score.opinion}
        mongo2.NotiHx(self.client).save(noti_data)

    def distribute_to_corps_db(self, dartinfo: DartInfo, cls: subjects.DartSubject, is_noti: bool):
        """
        개별 종목의 분석 데이터를 각 종목의 데이터베이스에 나눠서 저장하는 함수
        """
        dart_data = {'rcept_no': dartinfo.rno,
                     'rcept_dt': dartinfo.rdt,
                     'report_nm': dartinfo.rtitle,
                     'point': cls.score.point,
                     'text': cls.score.opinion,
                     'is_noti': is_noti}
        logger.debug(f'dartinfo.code : {dartinfo.code}')
        logger.debug(f'dart_data : {dart_data}')
        mongo2.CDart(self.client, dartinfo.code).save(dart_data)

    def run(self):
        """
        subject 에 해당하는 공시 타이틀을 분석한다.

        1. opendart 사이트의 연결여부 확인
        2. dartinfo 리스트의 개별 dartinfo 를 인자로 넣어 분석하여 포인트가 기준을 넘으면 노티하고 불필요하게 재분석을 방지하기 위해 피클에 저장한다.

        Returns:
            bool: 분석 성공 실패여부 리턴
        """
        t = len(self.dartinfo_list)

        for i, dartinfo in enumerate(self.dartinfo_list):
            print("*" * 80)
            print(f"{i + 1}/{t}. code: {dartinfo.code}\tname: {dartinfo.name}")

            # 분석하기 전 미리 넘어가도 되는 종목(신규종목, 이미분석된것, 스팩주..)들을 선별하여 미리 넘어간다...
            if not self.pre_ansys_test(dartinfo=dartinfo):
                continue

            print("-" * 80)
            print(dartinfo)
            # 분석 시행하고 피클 analysed 에 저장한다..

            subject_cls = getattr(subjects, self.subject)(self.client, self.driver, dartinfo)
            subject_cls.run()
            self.pickle.contents.analysed.append(dartinfo.rno)

            # 분석후 포인트가 노티포이트를 넘기고 거래정지 종목이 아니고 red price 가 0보다 큰 종목이면 노티한다.
            logger.info(f'<< subject_cls.score >>')
            logger.info(subject_cls.score)

            if subject_cls.score.point >= subjects.DartSubject.NOTI_POINT:
                if not self.is_trading_halt(dartinfo.code, self.driver):
                    _, 괴리율 = score.red(self.client, dartinfo.code)
                    if 괴리율 < 0:
                        is_noti = True
                        self.notify_and_write_record(dartinfo=dartinfo, cls=subject_cls)
                        self.pickle.contents.notified.append(dartinfo.rno)
                    else:
                        is_noti = False
                else:
                    is_noti = False
            else:
                is_noti = False

            # 각 해당코드의 corp db에 분산해서 저장한다.
            self.distribute_to_corps_db(dartinfo=dartinfo, cls=subject_cls, is_noti=is_noti)

            # 5개 단위로 분석이 완료되면 피클에 저장한다.
            if (i != 0) and (i % 5) == 0:
                print('Saving to pickle...')
                self.pickle.save()
        print('Saving to pickle...')

        # 한 타이틀이 끝나면 피클에 저장한다.
        self.pickle.save()


def run_all_subjects(edate: str) -> int:
    """전체 공시 분석
    enabled_subject 에 설정된 전자공시 제목을 하나하나 분석한다.

    내부적으로 피클을 사용하며 edate 에 해당하는 저장된 피클 자료가 있으면

    Args:
        edate (str): 분석을 원하는 날짜

    Returns:
        int: 분석 완료 후 소요시간 (초)
    """
    client = mongo2.connect_mongo(dbpath.load())

    status, message = Dart(client).server_test(edate)
    if status == '000':
        driver = utils.get_driver()
        pkl = Pickle()
        if pkl.contents.date != edate:
            # 피클에 세팅된 date 가 입력된 edate 와 다른 날짜의 경우 피클을 리셋한다.
            pkl.init(edate)
            pkl.load()

        print(f'Titles - {enabled_subject}')
        start_time = time.time()
        print('*' * 40, 'Dart analysis all titles', '*' * 40)
        try:
            for subject in enabled_subject:
                AnalyseOneSubject(client, driver, edate=edate, subject=subject, pkl=pkl).run()
        except Exception as e:
            # https://stackoverflow.com/questions/1483429/how-to-print-an-exception-in-python
            import traceback
            traceback.print_exc()
            noti.telegram_to(botname='dart', text=f"Exception occurred during AnalyseOneSubject() : {e}")
        finally:
            if driver is not None:
                # https://stackoverflow.com/questions/15067107/difference-between-webdriver-dispose-close-and-quit#:~:text=Close()%20%2D%20It%20is%20used,(Close%20all%20the%20windows).
                print("Retrieving webdriver...")
                driver.quit()
        print(pkl.contents)
        end_time = int(time.time() - start_time)
        print(f'Total spent time : {end_time} sec.')
        return end_time
    elif status == '013':
        # 013 :조회된 데이타가 없습니다.의 경우 - 공휴일
        logger.error(f'{status}: {message}')
        return 0
    else:
        logger.error(f'{status}: {message}')
        noti.telegram_to(botname='dart', text=f'{status}: {message}')
        return 0


if __name__ == '__main__':
    client = mongo2.connect_mongo(dbpath.load())
    driver = utils.get_driver()
    edate = '20220310'
    run_all_subjects(edate)

    """
    client = mongo2.connect_mongo(dbpath.load())
    driver = utils.get_driver()
    edate = '20220310'
    p = Pickle()
    print(p.contents)
    if p.contents.date != edate:
        # 피클에 세팅된 date가 입력된 edate와 다른 날짜의 경우 피클을 리셋한다.
        p.init(edate)
        p.load()
    AnalyseOneSubject(client, driver, edate=edate, subject='매출액또는손익', pkl=p).run()
    print(p.contents)
    """