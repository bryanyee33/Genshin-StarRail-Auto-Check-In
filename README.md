**Usage**
Make a fork of the repository first

Genshin Check in page:
https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481

Star Rail Check in page:
https://act.hoyolab.com/bbs/event/signin/hkrpg/index.html?act_id=e202303301540311

1. Go to either website
2. Press f12 to open development console
3. In the console, type: document.cookie
4. Copy the cookie into Settings -> Secrets and variables -> Actions -> New repository secret
   with Name as OS_COOKIE and Secret as the copied cookie
5. Deploy & Profit

All credits go to https://github.com/atomicptr/hoyo-daily-logins-helper.
Modified script to make it simpler & auto checkin both Genshin and Star Rail accounts at once.
Runs daily at 4.01am & 4.01pm (+8 UTC); twice to ensure that it checks in incase of issues
