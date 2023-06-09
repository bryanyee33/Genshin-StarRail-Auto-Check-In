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
5. Profit

Notes:
For multiple accounts, separate the cookies with "#" (no quotes and spaces between the cookies).
To specify games per account, add a new repository secret "GAME_CHOICE", by using "," to separate the games, and "#" to separate the accounts.

Eg: genshin,themis#starrail,honkai
where account 1 (based on cookie order) checks in for genshin and themis, and account 2 checks in for starrail and honkai

If "GAME_CHOICE" is used, all accounts require their games to be specified.

All credits go to https://github.com/atomicptr/hoyo-daily-logins-helper.
Modified script to make it simpler & auto checkin both Genshin and Star Rail accounts at once.
Runs daily at 4.01am (+8 UTC)
