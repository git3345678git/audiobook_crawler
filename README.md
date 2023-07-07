# audiobook_crawler

###這是某聽書網的爬蟲。目的在爬取每一集 m4a link<br/>
由於很久沒寫爬蟲，這算是複習。<br/>


網頁很賊的使用動態頁面，要從靜態頁面找出request 是不可能得，我用了 selenium 也沒抓到。<br/>
最後用了burpsuite 分析找到了關鍵請求。<br/>

### 腳本使用:
1. 使用 get_all_single_page.py 會生成一個data.json 。<br/>
裡面例出了每一集的關鍵請求<br/>

2. 使用 get_download_link.py  他會生成一個 download_list.json<br/>
裡面例出了每一集的 .m4a link<br/>

### 注意:
腳本中的http header　你要自己更換

### 心得:
這是個試用版，許多地方要改進!

1. 網站會block 規則有點嚴格，有些link 可以找到，有寫則是出現 cdn 的 block link <br/>
他不ban ip，我用4G，電腦上不同瀏覽器都會同時被檔，但手機上又可以。

2. 未來應該加上fake-useragent

3. 不應該一次抓取完在送到 download_list.json 應該每抓到一筆就記錄，這樣之後才可以記錄爬取到哪一集。

4. 下次嘗試使用 callback 再加上多線程。
