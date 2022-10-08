# 前置
程式需要的package都在requirement.txt裡了。用下面的指令就可以安裝。  
```pip3 install -r requirements.txt```

! tkinter needs another step, ```sudo apt install python3-tk```  

我Python的版本為"3.10.6"。pip的版本為"22.2.2"。  

用這個指令可以打開程式```python3 hw1.py```。

# 程式結構
## HW1
主要的影像處理函式都在imageop.py這個檔案中，我主要利用PIL中Image物件中的getpixel及putpixel來對圖片的灰階值操作。  
imageop.py的前三個函式都是調灰階值，分別是線性(g(x,y)=af(x,y)+b)、指數(g(x,y)=exp(af(x,y)+b))、取log(g(x,y)=ln(af(x,y)+b))，接著是graylevel slicing，用使用者給的範圍，將這個範圍的灰階值改成使用者要的值，並根據使用者選擇是否保留其他灰階值。  
再來是負片(我多寫的)，利用g(x,y)=255-f(x,y)得到新的灰階值。  
最後兩個則是放大縮小及旋轉操作，放大我是用"放大多少percentage"來指定縮放的scale，並且是用bilinear interpolation來縮放；旋轉操作則是用Image物件中的rotate函式處理。  

接著是Canv.py，主要處裡GUI中的畫布以及與使用者互動，負責顯示image、詢問使用者的需求、對未定義的數值處理、開啟與儲存image。  
而dialog.py是Canv.py在與使用者互動的小module，負責彈出對話框、回傳值。  

最後hw2.py則是主程式，但是沒在幹嘛，因為主要邏輯部分都在Canv.py以及imageop.py了，在hw2.py中只是定義GUI的排版而已。  
為了不讓按鈕等元件撞到image，所以我是用menu tools來對image操作。這樣的好處是可以讓image有更大的空間，且未來新增功能極為快速，但缺點則是使用起來沒很方便。

## HW2
這次在imageop.py中新增auto_level(img)、ravel(img)、bit_slicing(img, i)、general_filter(img, mask, rang, regu)、average_filter(img, rang)、sharpen_filter(img, k)、median_filter(img, rang)、Laplacian_filter(img)。  
- auto_level(img)就是histogram equalization，首先統計各灰階值出現的次數，接著計算prefix sum，再根據input的值對應到prefix sum、乘上(L-1)/(MN)就可以得到新的灰階值。  
- ravel(img)是auto_level(img)以及畫histogram的輔助函式，用來將圖片的灰階值轉成一維的list。  
- bit_slicing(img, i)利用g(x, y) = f(x, y) & (1 << i)這個公式來獲得圖片的第i個bit。  
- general_filter(img, mask, rang, regu)是一個spatial filter，可以自訂mask的權重、大小，以及是否要將結果除以權重總和。這個函式主要是輔助average_filter、Laplacian_filter。  
- average_filter(img, rang)是一個mask權重全為1的spatial filter，可以自訂mask的大小。  
- sharpen_filter(img, k)是利用unsharp masking的影像銳化函式，當k=1時，就是unsharp masking，當k>1時，就是highboost filtering。  
- median_filter(img, rang)會找出範圍中的中值，並更新g(x,y)。  
- Laplacian_filter(img)利用Laplacian mask來銳化影像。mask為  
[1, 1, 1]  
[1,-8, 1]  
[1, 1, 1]  

Canv.py新增上述功能的接口，不過多描述。

hw2.py也只是新增新功能的menu tools而已，不過多解釋。
