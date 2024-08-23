from instascrape import Reel
import time

SESSIONID = "Paste session Id Here"

headers = {
	"User-Agent": "'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'",
	"cookie": f'sessionid={SESSIONID};'
}
insta_reel = Reel(
	'')

insta_reel.scrape(headers=headers)

insta_reel.download(fp=f".\\Desktop\\reel{int(time.time())}.mp4")

print('Downloaded.')
