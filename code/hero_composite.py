from PIL import Image, ImageDraw, ImageFont
import os
PKG=os.path.expanduser("~/workspace/goals/daily-civic-data-brief/hidden_files/nashville-311-brief-2026-11-08")
src=os.path.join(PKG,"hero_source/media-generation-hero-art-nashville-311-0-dca1c960-2b0b-4e36-9a7f-b4332a3b7c3a.webp")
img=Image.open(src).convert("RGB"); W,H=img.size
scrim=Image.new("L",(1,int(H*0.42)),0)
for y in range(int(H*0.42)): scrim.putpixel((0,y), int(215*(1-y/(H*0.42))))
scrim=scrim.resize((W,int(H*0.42)))
black=Image.new("RGB",(W,int(H*0.42)),(18,18,18))
img.paste(Image.composite(black, img.crop((0,0,W,int(H*0.42))), scrim), (0,0))
d=ImageDraw.Draw(img)
def font(sz):
    return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",sz)
x=int(W*0.045)
d.text((x,int(H*0.045)),"21.1%",font=font(int(H*0.115)),fill=(232,163,61))
d.text((x,int(H*0.175)),"of Nashville's closed property-violation 311 requests",font=font(int(H*0.040)),fill=(245,245,245))
d.text((x,int(H*0.225)),"in 2025 took more than 30 days to close",font=font(int(H*0.040)),fill=(245,245,245))
d.text((x,int(H*0.295)),"hubNashville 311 - 248,066 requests opened in 2025  |  Machine Readable",font=font(int(H*0.021)),fill=(180,220,215))
img.save(os.path.join(PKG,"hero.png"))
open(os.path.join(PKG,"hero-headline.txt"),"w").write("21.1% of Nashville's closed property-violation 311 requests in 2025 took more than 30 days to close (4,343 of 20,564 closed property-violation requests)\nSource line: hubNashville 311 - 248,066 requests opened in 2025 | Machine Readable\n")
print(img.size)
