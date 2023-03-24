import time

from clean_database import cleanup_link_database
from config import CLEANUP_CYCLE, DATABASE_TXT, SCAN_INTERVAL_SECS
from filter_ads import filter_ads
from telegram_bot import send_ad
from upwork_logic import upwork_ad_collector


def gather_send_ads():
    i = 0

    while True:
        # ilanlari topla
        ads = upwork_ad_collector()

        # temizle
        ads = filter_ads(ads)

        #  gonder
        for ad in ads:
            send_ad(ad)

        # clean db
        if i > CLEANUP_CYCLE:
            cleanup_link_database(DATABASE_TXT)
            i = 0
        else:
            i = i + 1

        time.sleep(SCAN_INTERVAL_SECS)


def main():
    cleanup_link_database(DATABASE_TXT)
    gather_send_ads()


if __name__ == "__main__":
    main()
