# 前置
程式需要的package都在requirement.txt裡了。用下面的指令就可以安裝。  
```pip3 install -r requirements.txt```

我Python的版本為"3.10.6"。pip的版本為"22.2.2"。  

用這個指令可以打開程式```python3 hw1.py```。

# 程式結構
主要的影像處理函式都在imageop.py這個檔案中，我主要利用PIL中Image物件中的getpixel及putpixel來對圖片的灰階值操作。  
imageop.py的前三個函式都是調灰階值，分別是線性、指數、取log，接著是graylevel slicing，用使用者給的範圍，將這個範圍的灰階值改成使用者要的值，並根據使用者選擇是否保留其他灰階值。  
再來是負片(我多寫的)，利用g(x,y)=255-f(x,y)得到新的灰階值。  
最後兩個則是放大縮小及旋轉操作，放大我是用"放大多少percentage"來指定縮放的scale，並且是用bilinear interpolation來縮放；旋轉操作則是用Image物件中的rotate函式處理。  

接著是Canv.py，主要處裡GUI中的畫布以及與使用者互動，負責顯示image、詢問使用者的需求、對未定義的數值處理、開啟與儲存image。  
而dialog.py是Canv.py在與使用者互動的小module，負責彈出對話框、回傳值。  

最後hw1.py則是主程式，但是沒在幹嘛，因為主要邏輯部分都在Canv.py以及imageop.py了，在hw1.py中只是定義GUI的排版而已。  
為了不讓按鈕等元件撞到image，所以我是用menu tools來對image操作。這樣的好處是可以讓image有更大的空間，但缺點則是使用起來沒很方便。
