# Dictionary of all paths to be clicked or used by the scraper
path_dict = {
    "popups": {
        "small_popup_xpath": "//*[@id='app']/div[1]/div[3]/button",
        "big_popup_xpath": "//*[@id='app']/div[1]/div[2]/div[2]/div[4]/div/div[3]/div[4]/button",
        "terms_popup_xpath": "//*[@id='app']/div[3]/div/button",
    },
    "objects_to_scrape": {
        "cars": "//a[contains(@class, 'line-clamp-1')]",
    },
    "body": {
        "phone_btn_xpath": "//button[.//span[contains(text(), 'Show phone')]]",
        "phone_location_css": ".font-bold.text-gray-650.font-size-14.text-nowrap",
        "price_css": '.flex.items-center.text-\[28px\].leading-\[1\].text-gray-800.font-bold.pr-\[4px\]',
        "status_css": '.d-flex.align-items-center.text-green-450.font-size-12.mb-16px.mb-m-0',
        "user_css": ".block.text-gray-800.font-medium.text-14.text-line-1",
        "vehicle_info_css": '.flex.flex-wrap.whitespace-nowrap.items-center',

    },
    "pagination": {
        "pagination_css": ".pagination > li:nth-child(5)"
    }

}



