# 互動式

## 環境需求
```
pip install groq
```

* API key: 到[groqcloud](console.groq.com)建立，並加入環境變數  

以Powershell7(pwsh)為範例（powershell是一樣的做法）：  
```
vim(或其他編輯器) $PROFILE
```  
> 如果檔案不存在，參考[關於配置檔- PowerShell](https://learn.microsoft.com/zh-tw/powershell/module/microsoft.powershell.core/about/about_profiles?view=powershell-7.4)  

加入
```
$Env:GROQ_API_KEY="<你的api_key>"
```  
再重開終端機

## 使用方式
```
python test.py
```

可選擇使用哪個模型

輸入`exit`即可離開

## 輸出
會將問答結果輸出至`chat.md`檔案，每次執行會將舊檔刪除

## 參考資料
[groq](https://console.groq.com/docs/quickstart)