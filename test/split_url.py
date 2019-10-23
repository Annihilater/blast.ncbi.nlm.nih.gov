#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/10/22 08:07
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : split_url.py

url1 = 'https://www.ncbi.nlm.nih.gov/stat?ancestorClassName=searchInfo%2Call%2Call%2Cblastp%2Cf-wrap-1%2Call&ancestorId=sopts%2CoptSection%2CsearchForm%2Ccontent%2Ccontent-wrap&blastButton=search&browserheight=1066&browserwidth=701&colorDepth=24&cookieSize=791&cookieenabled=true&eventid=0&ga_label=NONE&is_browser_supported=true&jsevent=click&link_action_name=%0A%20%20%20%20%0A%20%20&link_category_name=&link_class=summary&link_href=&link_id=blastButton1&link_name=&link_ref=&link_section_name=&link_sid=&link_text=%0A%20%20%20%20%0A%20%20&myncbi_signed_in=true&ncbi_algorithm=&ncbi_app=blast&ncbi_db=&ncbi_featured_srcdb=&ncbi_nwds=&ncbi_pcid=&ncbi_pdid=blastsearch&ncbi_phid=55BA5057DADA56810000000000000001&ncbi_program=blastp&ncbi_sessionid=5AAB49C2DAD5CBD1_0000SID&ncbi_stat=false&ncbi_timesinceload=17225&ncbi_timesincenavstart=26793&pagename=blast%3A%3Ablastsearch%3ANONE&screenavailheight=1177&screenavailwidth=1920&screenheight=1200&screenwidth=1920&server=blast.ncbi.nlm.nih.gov&sgSource=api&sgversion=0.26.1&sgversion_hotfix=1&sgversion_major=0&sgversion_minor=26&spa_index=0'
url2 = 'https://www.ncbi.nlm.nih.gov/stat?browserheight=1066&browserwidth=701&canscroll_x=true&canscroll_y=true&colorDepth=24&cookieSize=1195&cookieenabled=true&eventid=1&is_browser_supported=true&jsevent=unload&jsloadtime=&jsperf_basePage=2951&jsperf_connect=3391&jsperf_dns=0&jsperf_navType=0&jsperf_redirectCount=0&jsperf_ttfb=3181&myncbi_signed_in=true&ncbi_algorithm=&ncbi_app=blast&ncbi_db=&ncbi_featured_srcdb=&ncbi_nwds=&ncbi_pcid=&ncbi_pdid=blastsearch&ncbi_phid=55BA5057DADA56810000000000000001&ncbi_program=blastp&ncbi_sessionid=5AAB49C2DAD5CBD1_0000SID&ncbi_stat=false&ncbi_timeonpage=&ncbi_timesinceload=17244&ncbi_timesincenavstart=26812&pagename=blast%3A%3Ablastsearch%3ANONE&screenavailheight=1177&screenavailwidth=1920&screenheight=1200&screenwidth=1920&server=blast.ncbi.nlm.nih.gov&sgSource=native&sgversion=0.26.1&sgversion_hotfix=1&sgversion_major=0&sgversion_minor=26&spa_index=0&version.jig=1.14.8&widget_ncbiautocomplete.jig=1&widget_ncbiexternallink.jig=1&widget_ncbihelpwindow.jig=1&widget_ncbipopper.jig=1&widget_ncbitoggler.jig=34&x.maxscroll=0&x.pagesize=12&y.maxscroll=3&y.pagesize=11'
url3 = 'https://blast.ncbi.nlm.nih.gov/t2g.cgi?CMD=Get&RID=UV9C3BYW01R&DESCRIPTIONS=0&NUM_OVERVIEW=0&GET_SEQUENCE=on&DYNAMIC_FORMAT=on&ALIGN_SEQ_LIST=pdb|5UBB|A,ref|NP_001129579.1|,ref|XP_024099608.1|,ref|XP_012299980.1|,ref|XP_003258907.1|&HSP_SORT=0&SEQ_LIST_START=1&QUERY_INDEX=0&ADV_VIEW=on&SHOW_LINKOUT=on&MASK_CHAR=2&MASK_COLOR=1&ALIGNMENT_VIEW=Pairwise&LINE_LENGTH=60'
url4 = 'https://blast.ncbi.nlm.nih.gov/t2g.cgi?CMD=Get&RID=UV9C3BYW01R&ADV_VIEW=on&DYNAMIC_FORMAT=on&QUERY_INDEX=0&FORMAT_OBJECT=TaxBlast&DESCRIPTIONS=&DESCRIPTIONS=100'
tmp = url4.split('&')
for item in tmp:
    print(item)
