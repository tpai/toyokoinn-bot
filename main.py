from playwright.sync_api import sync_playwright

import os
import socket

is_production= os.getenv("IS_PRODUCTION", "true")
chrome_hostname = os.getenv("CHROME_HOSTNAME", "localhost")
tokyoinn_email = os.getenv("TOKYOINN_EMAIL", "")
tokyoinn_password = os.getenv("TOKYOINN_PASSWORD", "")
phone_number = os.getenv("PHONE_NUMBER", "")
checkin_date = os.getenv("CHECKIN_DATE", "2025/08/04")
checkin_time = os.getenv("CHECKIN_TIME", "22:00:00")
stay_nights = os.getenv("STAY_NIGHTS", "1")
guests = os.getenv("GUESTS", "2")
room_type = os.getenv("ROOM_TYPE", "")
smoke_room = os.getenv("SMOKE_ROOM", "")
rooms = os.getenv("ROOMS", "1")
area = os.getenv("AREA", "12")
hotel = os.getenv("HOTEL", "00087")
person_per_room = os.getenv("PERSON_PER_ROOM", "2")

def run(playwright):
    if is_production == "true":
        ip_address = socket.gethostbyname(chrome_hostname)
        browser = playwright.chromium.connect_over_cdp(f"http://{ip_address}:9222")
    else:
        browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto("https://www.toyoko-inn.com/?lcl_id=ja")
    page.goto("https://www.toyoko-inn.com/login")

    page.fill('input[name="mail"]', tokyoinn_email)
    page.fill('input[name="password"]', tokyoinn_password)
    page.click('input[type="submit"]')

    page.wait_for_url('**/index*')

    page.goto("https://www.toyoko-inn.com/search/")

    page.evaluate(f"""
        () => {{
            $('#datepicker').val('{checkin_date}');
        }}
    """)
    page.select_option('select[name="inn_date"]', value=stay_nights)
    page.select_option('select[name="sel_ldgngPpl"]', value=guests)
    page.select_option('select[name="sel_room_clss_Id"]', value=room_type)
    page.select_option('select[name="rd_smk"]', value=smoke_room)
    page.select_option('select[name="rsrv_num"]', value=rooms)
    page.select_option('select[name="sel_area"]', value=area)
    page.select_option('select[name="sel_htl"]', value=hotel)

    page.click('a[class*="js-form-action"]')

    page.wait_for_url('**/room*')

    availableRooms = page.locator('a[onclick^="submitReserve"]')
    roomCount = availableRooms.count()

    if roomCount > 0:
        firstRoom= availableRooms.first
        firstRoom.click()

        page.wait_for_url('**/input*')

        page.locator('input[name="purpose_of_use"][value="0"]').check()
        page.select_option('select[name="room[0][prsn_num]"]', value=person_per_room)
        page.fill('input[name="room[0][tlpn]"]', phone_number)
        page.select_option('select[name="room[0][checkin_tm]"]', value=checkin_time)
        page.click('a[class*="jsBtnCnfrm"]')

        page.wait_for_url('**/confirm*')

        page.locator('input[name="agreeCheck"]').check()
        page.click('input[type="submit"]')

        page.wait_for_url('**/finish*')
        print("Booking successful.")
    else:
        print("No rooms available.")

    page.screenshot(path="screenshot.png", full_page=True)

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
