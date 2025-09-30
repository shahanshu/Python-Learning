

from langchain_community.document_loaders import WebBaseLoader
get= WebBaseLoader("https://www.daraz.com.np/products/sunset-lamp-light-lamp-rainbow-floor-lamp-sun-never-sets-projection-night-light-with-stand-usb-charging-wall-decoration-light-i181415091-s1212320529.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253A%253Bnid%253A181415091%253Bsrc%253ALazadaMainSrp%253Brn%253A742868779ac86a7822e5731f96d382d4%253Bregion%253Anp%253Bsku%253A181415091_NP%253Bprice%253A726%253Bclient%253Adesktop%253Bsupplier_id%253A900265424721%253Bbiz_source%253Ah5_external%253Bslot%253A0%253Butlog_bucket_id%253A470687%253Basc_category_id%253A10000641%253Bitem_id%253A181415091%253Bsku_id%253A1212320529%253Bshop_id%253A174733%253BtemplateInfo%253A-1_A3_C%25231103_L%2523&freeshipping=0&fs_ab=1&fuse_fs=&lang=en&location=Bagmati%20Province&price=726&priceCompare=skuId%3A1212320529%3Bsource%3Alazada-search-voucher%3Bsn%3A742868779ac86a7822e5731f96d382d4%3BoriginPrice%3A72600%3BdisplayPrice%3A72600%3BsinglePromotionId%3A50000018794008%3BsingleToolCode%3ApromPrice%3BvoucherPricePlugin%3A0%3Btimestamp%3A1759046505435&ratingscore=5.0&request_id=742868779ac86a7822e5731f96d382d4&review=1&sale=7&search=1&source=search&spm=a2a0e.searchlistcategory.list.0&stock=1")


load= get.load()
print(type(load))                  
print(len(load))
print(load[0].page_content)