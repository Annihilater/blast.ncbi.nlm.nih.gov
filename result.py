#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/10/23 11:16
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : result.py

import requests


def get_result(rid):
    """
    通过 rid 获取结果
    :param rid:
    :return:
    """
    url = "https://blast.ncbi.nlm.nih.gov/Blast.cgi"
    headers = {
        'authority': "blast.ncbi.nlm.nih.gov",
        'pragma': "no-cache",
        'cache-control': "no-cache,no-cache",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        'sec-fetch-mode': "navigate",
        'sec-fetch-user': "?1",
        'origin': "https://blast.ncbi.nlm.nih.gov",
        'content-type': "application/x-www-form-urlencoded",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        'sec-fetch-site': "same-origin",
        'referer': "https://blast.ncbi.nlm.nih.gov/Blast.cgi",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
        'cookie': "MyBlastUser=1-K62_H2PRYnAJWAW8C499055; ncbi_sid=5AAB49C2DAD5CBD1_0000SID; _ga=GA1.2.1760716258.1571642619; _gid=GA1.2.1120047674.1571642619; _ga=GA1.3.1760716258.1571642619; _gid=GA1.3.1120047674.1571642619; QSI_HistorySession=https%3A%2F%2Fwww.nlm.nih.gov%2F%23~1571655071695; ___rl__test__cookies=1571655469341; OUTFOX_SEARCH_USER_ID_NCOO=1690574555.305844; books.article.report=; MyNcbiSigninPreferences=O25jYmlscyY%3D; ncbi_prevPHID=CE8CB87BDAD9B9910000000000110007.m_8.09; WebCubbyUser=YFK36EUALZSLFML717L8VTJ8L7VZ587M%3Blogged-in%3Dtrue%3Bmy-name%3Dyanmiexingkong%3Bpersistent%3Dfalse%405AAB49C2DAD5CBD1_0000SID; BlastCubbyImported=active; ncbi_pinger=N4IgDgTgpgbg+mAFgSwCYgFwgKwEFcBCALAJwDCATACK5XZkFUkCM2A7Mx6UcwGzbYAygEkqIADQgArgDsANgHsAhqhlQAHgBdMoCphAAjOUoDO2yQGZ9MiBJBFrUAO5HTm6CalzNJu9n12nPoAZkpyJlB2FAAM+tjRZCQWFKw0AKK8ABy4LNF5+QWFzFHFWK5mGDaVzuXuUJ7eJhgAcgDyzWlRemXGZgB0MgDGBsgDcgC2A8iIfQDmCjBRJPrMJDF2FrFYzDGxlqUgq+uW3YecbBtWWKHhkZYOWO5SdyAWmQGWy1i8JD8kbFZJEQtiAfmxeGwKBcgVcQNE+hReH1ikCHtJ5MpVBpzPZ/Ns/LDMmwHJJsGjmNFeLw/NTttgKHpSRcsHtQQcAQ4AL6coA,MyBlastUser=1-K62_H2PRYnAJWAW8C499055; ncbi_sid=5AAB49C2DAD5CBD1_0000SID; _ga=GA1.2.1760716258.1571642619; _gid=GA1.2.1120047674.1571642619; _ga=GA1.3.1760716258.1571642619; _gid=GA1.3.1120047674.1571642619; QSI_HistorySession=https%3A%2F%2Fwww.nlm.nih.gov%2F%23~1571655071695; ___rl__test__cookies=1571655469341; OUTFOX_SEARCH_USER_ID_NCOO=1690574555.305844; books.article.report=; MyNcbiSigninPreferences=O25jYmlscyY%3D; ncbi_prevPHID=CE8CB87BDAD9B9910000000000110007.m_8.09; WebCubbyUser=YFK36EUALZSLFML717L8VTJ8L7VZ587M%3Blogged-in%3Dtrue%3Bmy-name%3Dyanmiexingkong%3Bpersistent%3Dfalse%405AAB49C2DAD5CBD1_0000SID; BlastCubbyImported=active; ncbi_pinger=N4IgDgTgpgbg+mAFgSwCYgFwgKwEFcBCALAJwDCATACK5XZkFUkCM2A7Mx6UcwGzbYAygEkqIADQgArgDsANgHsAhqhlQAHgBdMoCphAAjOUoDO2yQGZ9MiBJBFrUAO5HTm6CalzNJu9n12nPoAZkpyJlB2FAAM+tjRZCQWFKw0AKK8ABy4LNF5+QWFzFHFWK5mGDaVzuXuUJ7eJhgAcgDyzWlRemXGZgB0MgDGBsgDcgC2A8iIfQDmCjBRJPrMJDF2FrFYzDGxlqUgq+uW3YecbBtWWKHhkZYOWO5SdyAWmQGWy1i8JD8kbFZJEQtiAfmxeGwKBcgVcQNE+hReH1ikCHtJ5MpVBpzPZ/Ns/LDMmwHJJsGjmNFeLw/NTttgKHpSRcsHtQQcAQ4AL6coA; ncbi_sid=5AAB49C2DAD5CBD1_0000SID; BlastCubbyImported=passive",
        'Postman-Token': "effbbf9e-09ff-4958-8a0e-a8c3d2719ae1,ffe9004f-7563-4ea5-ad02-943a343657a8",
        'Host': "blast.ncbi.nlm.nih.gov",
        'Content-Length': "1354",
        'Connection': "keep-alive"
    }
    data = {'ADV_VIEW': 'true', 'ALIGNMENTS': '100', 'ALIGNMENT_VIEW': 'Pairwise', 'BLAST_PROGRAMS': 'blastp',
            'CDD_RID': 'UWU3DJDS015', 'CDD_SEARCH_STATE': '2', 'CLIENT': 'web', 'COMPOSITION_BASED_STATISTICS': '2',
            'CONFIG_DESCR': '2%2C3%2C4%2C5%2C6%2C7%2C8', 'DATABASE': 'nr_v5', 'DB_DISPLAY_NAME': 'nr',
            'DESCRIPTIONS': '100', 'EQ_OP': 'AND', 'EXPECT': '10', 'FILTER': 'F', 'FORMAT_NUM_ORG': '1',
            'FORMAT_OBJECT': 'Alignment', 'FORMAT_TYPE': 'HTML', 'FULL_DBNAME': 'nr_v5', 'GAPCOSTS': '11%2B1',
            'GET_SEQUENCE': 'true', 'HSP_RANGE_MAX': '0', 'JOB_TITLE': '%2B5ubb%2B', 'LAYOUT': 'OneWindow',
            'LINE_LENGTH': '60', 'MASK_CHAR': '2', 'MASK_COLOR': '1', 'MATRIX_NAME': 'BLOSUM62', 'MAX_NUM_SEQ': '100',
            'NCBI_GI': 'false', 'NEW_VIEW': 'true', 'NUM_DIFFS': '0', 'NUM_OPTS_DIFFS': '0', 'NUM_ORG': '1',
            'NUM_OVERVIEW': '100', 'ORG_DBS': 'giless_dbvers5', 'PAGE': 'Proteins', 'PAGE_TYPE': 'BlastSearch',
            'PROGRAM': 'blastp',
            'QUERYFILE': '%3E5ubb%0D%0ASQVINGEMQFYARAKLFYQEVPATEEGMMGNFIELSSPDIQASQKFLRKFVGGPGRAGTDCALDCGSGIGRVSKHVLLPVFNSVELVDMMESFLLEAQNYLQVKGDESYHCYSLQEFTPPFRRYDVIWIQWVSGHLTDKDLLAFLSRCRDGLKENGIIILKDNVAREGCILDLSDSSVTRDMDILRSLIRKSGLVVLGQEKQDGFPEQCIPVWMFALH%0D%0A',
            'QUERY_INFO': '%2B5ubb%2B', 'QUERY_LENGTH': '218', 'REPEATS': '45518', 'RTOE': '27',
            'SAVED_SEARCH': 'true', 'SEARCH_DB_STATUS': '31', 'SELECTED_PROG_TYPE': 'blastp', 'SERVICE': 'plain',
            'SHORT_QUERY_ADJUST': 'on', 'SHOW_CDS_FEATURE': 'false', 'SHOW_LINKOUT': 'true', 'SHOW_OVERVIEW': 'true',
            'UNIQ_DEFAULTS_NAME': 'A_SearchDefaults_1iMhfz_1v71_duIAy0mW1FA_GTXQl_2J8uR3', 'USER_DEFAULT_MATRIX': '4',
            'USER_DEFAULT_PROG_TYPE': 'blastp', 'USER_TYPE': '1', 'WORD_SIZE': '6', '_PGR': '6', 'db': 'protein',
            'stype': 'protein', 'CMD': 'Get'}
    data.update({'RID': rid})

    response = requests.post(url=url, data=data, headers=headers)
    html = response.text

    with open('data/html/result.html', 'w') as f:
        f.write(html)


if __name__ == '__main__':
    rid = 'UX0VYAFM015'
    rid2 = 'UXTZXYRW015'
    rid3 = 'V019SAM701R'
    get_result(rid3)
