from playwright.sync_api import sync_playwright

import os
import time
import socket

is_production= os.getenv("IS_PRODUCTION", "true")
chrome_hostname = os.getenv("CHROME_HOSTNAME", "localhost")
tokyoinn_email = os.getenv("TOKYOINN_EMAIL", "")
tokyoinn_password = os.getenv("TOKYOINN_PASSWORD", "")
phone_number = os.getenv("PHONE_NUMBER", "")
checkin_date = os.getenv("CHECKIN_DATE", "2025-08-07")
checkout_date = os.getenv("CHECKOUT_DATE", "2025-08-08")
checkin_time = os.getenv("CHECKIN_TIME", "22:00:00")
rooms = os.getenv("ROOMS", "1")
guests = os.getenv("GUESTS", "2")
room_type = os.getenv("ROOM_TYPE", "20")
smoke = os.getenv("SMOKE", "noSmoking") # smoking, noSmoking, all
hotel = os.getenv("HOTEL", "00319")

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

    page.fill('input[name="email"]', tokyoinn_email)
    page.fill('input[name="password"]', tokyoinn_password)
    page.click('div.login_buttons__zMG9U button:first-child')

    page.locator('button.HeaderNavPC_mypage-link__3Tnzt').wait_for()

    page.goto(f"https://www.toyoko-inn.com/search/result/room_plan/?hotel={hotel}&start={checkin_date}&end={checkout_date}&room={rooms}&people={guests}&smoking=noSmoking&roomType={room_type}&tab=roomType&sort=recommend")

    page.wait_for_url('**/room_plan/*')

    availableRooms = page.locator('div.SearchResultRoomPlanChildCard_price-section__D0DAr button')
    roomCount = availableRooms.count()

    if roomCount > 0:
        firstRoom= availableRooms.first
        firstRoom.click()
        time.sleep(1)

        # close popup
        page.locator('label[for="student-plan-agreement"]').check()
        page.locator('div.Dialog_buttons__Sk9_O > button:first-child').click()

        page.wait_for_url('**/reservations/*')

        page.locator('input[name="purpose_of_use"][value="0"]').check()
        page.fill('input[name="room[0][tlpn]"]', phone_number)
        page.select_option('select[name="room[0][checkin_tm]"]', value=checkin_time)
        page.click('p#cnfrm')

        page.wait_for_url('**/confirm*')

        page.locator('input[name="agreeCheck"]').check()
        page.click('input[type="submit"]')

        page.wait_for_url('**/finish*')
        print(f"Booking successful\n> Check-in: {checkin_date}T{checkin_time}|Rooms: {rooms}|Guests: {guests}|Type: {room_type}|Smoke: {smoke}|Hotel: {hotel}")
    else:
        print(f"No rooms available\n> Check-in: {checkin_date}T{checkin_time}|Rooms: {rooms}|Guests: {guests}|Type: {room_type}|Smoke: {smoke}|Hotel: {hotel}")

    if is_production != "true":
        page.screenshot(path="screenshot.png", full_page=True)

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
