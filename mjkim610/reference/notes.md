#### Feature category
- Lexical based
- Keyword based
- Search engine based
- Reputation based

#### Lexical-based features
- Port number in url
- Length of host (Max for non-phishing was 70, while 240 for phishing. So may be we can have 2 features for length, one for actual length and one for whether it exceeds 70.)
- Number of `.` in host (Same logic as above, non-phishing max was 5.)
- Length of URL (Same logic as above, non-phishing max was 383.)

*Will have to check for any patterns specific to Naver*
- `-` in host
- `[0-9]` in host
- IP based host
- Hex based host
- Encoding is different (Cyrillic, etc.)

- `-`, `=`, `/`, `;`, `,`, etc. in path
- Has parameter part
- Has fragment part (what is fragment?)
- `username` in URL
- `password` in URL

#### Keyword-based features
- Contains `log`, `pay`, `web`, `cmd`, `account`, `dispatch`, `free`, `run`, `net`, `confirm`, etc.

#### Reputation-based features
- PhishTank, StopBadware, etc.

#### Search engine-based features
- URL not in Google top results

----
#### Other ideas
- Is it possible to determine whether a page has popups by looking at its front-end code? JS?
- Is is possible to attempt to enter fake credentials which will let me log in, instead of redirecting me to a 'login failed' page?
- Check if https certificate is from the same provider, or check if the certificate is the one that is issued by Naver (if the number of certificates is manageable)
- Check last two keywords in the domain (right before the `/`)
- Maybe check raw length of code, or the validity of referenced resources