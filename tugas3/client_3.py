import logging
import requests
import os
import threading


def download_gambar(url=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        # ekstensi = tipe[content_type]
        # logging.warning(f"writing {namafile}.{ekstensi}")
        logging.warning(f"writing {namafile}")
        # fp = open(f"{namafile}.{ekstensi}","wb")
        fp = open(f"{namafile}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False




if __name__=='__main__':
    # download_gambar('https://asset.kompas.com/crops/qz_jJxyaZgGgboomdCEXsfbSpec=/0x0:998x665/740x500/data/photo/2020/03/01/5e5b52f4db896.jpg')

    link_gambar = []
    link_gambar.append('https://asset.kompas.com/crops/qz_jJxyaZgGgboomdCEXsfbSpec=/0x0:998x665/740x500/data/photo/2020/03/01/5e5b52f4db896.jpg')
    link_gambar.append('https://media.suara.com/pictures/480x260/2019/12/26/49091-gambar.jpg')
    link_gambar.append('https://www.provoke-online.com/images/art_news/a35e4adffa4eb4891062bb42.jpg')
    link_gambar.append('https://www.mastekno.com/wp-content/uploads/2019/10/gambar-sketsa.jpg')

    threads = []
    for i in range(4):
        t = threading.Thread(target=download_gambar,args=(link_gambar[i],))
        threads.append(t)
    
    for thr in threads:
        thr.start()