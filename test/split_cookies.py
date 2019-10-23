#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/10/22 08:30
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : split_cookies.py

cookies = 'MyBlastUser=1-K62_H2PRYnAJWAW8C499055; ncbi_sid=5AAB49C2DAD5CBD1_0000SID; _ga=GA1.2.1760716258.1571642619; _gid=GA1.2.1120047674.1571642619; _ga=GA1.3.1760716258.1571642619; _gid=GA1.3.1120047674.1571642619; QSI_HistorySession=https%3A%2F%2Fwww.nlm.nih.gov%2F%23~1571655071695; ___rl__test__cookies=1571655469341; OUTFOX_SEARCH_USER_ID_NCOO=1690574555.305844; books.article.report=; MyNcbiSigninPreferences=O25jYmlscyY%3D; ncbi_prevPHID=CE8CB87BDAD9B9910000000000110007.m_8.09; WebCubbyUser=YFK36EUALZSLFML717L8VTJ8L7VZ587M%3Blogged-in%3Dtrue%3Bmy-name%3Dyanmiexingkong%3Bpersistent%3Dfalse%405AAB49C2DAD5CBD1_0000SID; BlastCubbyImported=active; WebEnv=1h1Mjs%405AAB49C2DAD5CBD1_0000SID; _gat_ncbiSg=1; _gat_dap=1; ncbi_pinger=N4IgDgTgpgbg+mAFgSwCYgFwgKzYEICC2ADNgOwAiBV2AbABwCMxLrb7jIANCAMYA2yXgGsAdlAAeAF0yhimEAGcoAQwi9EASVEAzAPZcV/foeNcARvxWKpYLjoC0AdwgqwDxqf7cQnLIr0wKUUuQKkAZSheKWQ9US5lNQ0AMT0IAFsuXjipKFEpLJy8qWdXMB8AZgBOBUYyACZ67B8AFnksetoyKorWloUBITFJGR4W5qx5MZr/AFd09LUATx8SBVW/EEtrKTxZqSk4zh5seoUAHVEAAhury5uQAF8eWdF+PRVUcWlZEArerBSCCzKCVfqA4GgngVejraEzXwNFr9MbtECdJhnMbgkCvd6fb6jEDjWqrWgKf5VY44MgKKYgWibCqMJhPHjZBZxQm/M5YbY2Spw4kKfnBVTqRCrIV1BQ6IzKHz1NG4QgkchUGgMZjsHWsan1TaijAYUWJCUYAByAHkLQBRRW8rZWGwAOlEvHMyDd/HSbuQiBdAHM9DBFQjGFUlZU0YwlfTmbVI/HHYw6rSxgCQMQXZ0XdTsJmyMR8zjmLRyY9HkA'

tmp = cookies.split('; ')
for item in tmp:
    print(item)


