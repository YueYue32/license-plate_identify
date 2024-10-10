# license-plate_identify

# 車牌辨識：使用pytesseract

#
安裝流程參考：https://lufor129.medium.com/pytesseract-%E8%BE%A8%E8%AD%98%E5%9C%96%E7%89%87%E4%B8%AD%E7%9A%84%E6%96%87%E5%AD%97-b1024f678fac

#

抓圖程式：images_dw.py

#

主程式：license-plate_identify.py

#

如果要辨識語言文字，可加入lang至下；
可使用加號辨識多種語言，例如要辨識中文 + 英文組合的文字，即為 lang="chi_tra+eng"
pytesseract.image_to_string(binary_image, config=custom_config,lang=)

常見的 lang 參數選項：
eng: 英文
chi_sim: 簡體中文
chi_tra: 繁體中文
jpn: 日文
kor: 韓文
fra: 法文
deu: 德文
spa: 西班牙文
rus: 俄文
ita: 義大利文
