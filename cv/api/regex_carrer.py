import re
from urllib import request
import requests
# data1 = """<html lang="en" data-ph-id="ph-page-element-page19-2fIsoJ" class="external en_us desktop"><!--<![endif]--><script async="" crossorigin="anonymous" type="text/javascript" src="https://cdnssl.clicktale.net/www32/ptc/b61598e7-9c00-482d-8d71-56d726c2f593.js"></script><script async="" src="https://www.googletagmanager.com/gtm.js?id=GTM-MP6J282"></script><script type="text/javascript" async="" src="//careers.microsoft.com/us/en/phenomtrack.min.js"></script><head data-ph-id="ph-page-element-page19-14VIOG"><meta name="layout" content="site-layout" data-ph-id="ph-page-element-page19-iTdu0p"><meta http-equiv="X-UA-Compatible" content="IE=edge, chrome=1" data-ph-id="ph-page-element-page19-bn1h2C"><link rel="next" href="https://careers.microsoft.com/us/en/search-results?keywords=php&amp;from=50&amp;s=1">
# <link rel="canonical" href="https://careers.microsoft.com/us/en/search-results?keywords=php">
#
#
#
#
#
#
#       <link type="image/x-icon" href="https://prodcmscdn.azureedge.net/careerconnectresources/p/MICRUS/en_us/desktop/assets/images/favicon.ico" rel="icon" data-ph-id="ph-page-element-page19-52XfJj">
#        <link rel="apple-touch-icon-precomposed" sizes="114x114" href="https://prodcmscdn.azureedge.net/careerconnectresources/p/MICRUS/en_us/desktop/assets/images/mobile/h/apple-touch-icon.png" data-ph-id="ph-page-element-page19-ntaOFI">
#         <link rel="apple-touch-icon-precomposed" sizes="72x72" href="https://prodcmscdn.azureedge.net/careerconnectresources/p/MICRUS/en_us/desktop/assets/images/mobile/m/apple-touch-icon.png" data-ph-id="ph-page-element-page19-pZawS2">
#          <link rel="apple-touch-icon-precomposed" href="https://prodcmscdn.azureedge.net/careerconnectresources/p/MICRUS/en_us/desktop/assets/images/mobile/l/apple-touch-icon-precomposed.png" data-ph-id="ph-page-element-page19-Y6o14n">
#           <link rel="shortcut icon" href="https://prodcmscdn.azureedge.net/careerconnectresources/p/MICRUS/en_us/desktop/assets/images/mobile/l/apple-touch-icon.png" data-ph-id="ph-page-element-page19-o8wQ7D">
#            <link rel="apple-touch-startup-image" href="https://prodcmscdn.azureedge.net/careerconnectresources/p/MICRUS/en_us/desktop/assets/images/mobile/l/splash.png" data-ph-id="ph-page-element-page19-Zl1GAm">
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#  <script type="text/javascript"> /*<!--*/ var phApp = phApp || {"widgetApiEndpoint":"https://careers.microsoft.com/widgets","country":"us","deviceType":"desktop","locale":"en_us","absUrl":true,"refNum":"MICRUS","cdnUrl":"https://prodcmscdn.azureedge.net/careerconnectresources/p","baseUrl":"https://careers.microsoft.com/us/en/","baseDomain":"https://careers.microsoft.com","phenomTrackURL":"careers.microsoft.com/us/en/phenomtrack.min.js","pageName":"search-results","siteType":"external","rootDomain":"https://careers.microsoft.com","pageId":"page19"}; phApp.ddo = {"siteConfig":{"status":"success","errorCode":null,"errorMsg":null,"data":{"urlMap":{"home":"home","category":"c/:category","job":"job/:jobSeqNo/:title","jobcart":"jobcart","search-results":"search-results","glassdoor-reviews":"glassdoor-reviews"},"categoryUrlMap":{"MICRUS_Legal---Corporate-Affairs":"c/legal-corporate-affairs-jobs","MICRUS_Supply-Chain---Operations-Management":"c/supply-chain-operations-management-jobs","MICRUS_Field-Business-Leadership":"c/field-business-leadership-jobs","MICRUS_Business-Programs---Operations":"c/business-programs-operations-jobs","MICRUS_Engineering":"c/engineering-jobs","MICRUS_Human-Resources":"c/human-resources-jobs","MICRUS_Marketing":"c/marketing-jobs","MICRUS_Technical-Sales":"c/technical-sales-jobs","MICRUS_Research":"c/research-jobs","MICRUS_Evangelism":"c/evangelism-jobs","MICRUS_Finance":"c/finance-jobs","MICRUS_Hardware-Manufacturing-Engineering":"c/hardware-manufacturing-engineering-jobs","MICRUS_Retail":"c/retail-jobs","MICRUS_Services":"c/services-jobs","MICRUS_Business-Development---Strategy":"c/business-development-strategy-jobs","MICRUS_Sales":"c/sales-jobs","MICRUS_Hardware-Engineering":"c/hardware-engineering-jobs","MICRUS_Product-Manufacturing-Operations":"c/product-manufacturing-operations-jobs","MICRUS_IT-Operations":"c/it-operations-jobs","MICRUS_Customer-Success":"c/customer-success-jobs","MICRUS_Data-Center":"c/data-center-jobs","MICRUS_Unassigned":"c/unassigned-jobs"},"siteSettings":{"skipLogout":true,"glassdoor":{},"glassdoorReviews":{},"twitter":{},"linkedIn":{"apiKey":"752xe1cieo8utv"},"dropbox":{"apiKey":"22zulv8zlv6dqam"},"referalUrl":"404","filePicker":{"onedrive":{"clientId":"8efc58d6-0c97-47a3-a8b1-092f87d54351","devkey":""},"dropbox":{"clientId":"zxqem6bqrgopvs0","devkey":""},"googledrive":{"clientId":"21747885378-4j2okdko0uuvqb4bacu2rvr1cjndt9l2.apps.googleusercontent.com","devkey":"AIzaSyBFrajIgOC9E6vnLy9n1YheaHkzGX7x1Dc"}},"disableJobFilters":true,"referrerParams":true,"applyprofile":{"flowurl":"https://apply.microsoft.com/authenticate/social","linkedin":"/linkedin","live_aad":"/microsoft-azuread","google":"/google","live":"/microsoft-live","facebook":"/facebook","fb":"/facebook"},"dynamics":{"flowurl":"https://offer.talent.dynamics.com/applicantlogin","domain_hint":{"linkedin":"linkedin.com","live_aad":"microsoft.com","google":"google.com","live":"live.com","facebook":"facebook.com","fb":"facebook.com"}},"oauth":{"google":{"loginUrl":"https://accounts.google.com/o/oauth2/auth","logoutUrl":"https://www.google.com/accounts/Logout?continue=https://appengine.google.com/_ah/logout","clientId":"95432501623-4s4d3s0f3m5e0eanp3fhro3f96itum5h.apps.googleusercontent.com","scope":"https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/user.phonenumbers.read","redirectUri":"/auth/g","response_type":"code"},"microsoftCorporate":{"loginUrl":"https://login.microsoftonline.com/72f988bf-86f1-41af-91ab-2d7cd011db47/oauth2/authorize","logoutUrl":"","clientId":"9c89dc9b-4ee6-46a9-9969-13d9e66f4c4f","redirectUri":"/iauth/ml","scope":"wl.basic wl.emails wl.phone_numbers","response_type":"code"},"microsoft":{"loginUrl":"https://login.live.com/oauth20_authorize.srf","logoutUrl":"","clientId":"000000004814DB1E","redirectUri":"/auth/ml","scope":"wl.basic wl.emails wl.phone_numbers wl.offline_access","response_type":"code"},"facebook":{"loginUrl":"https://www.facebook.com/dialog/oauth","logoutUrl":"","clientId":"553656317993885","redirectUri":"/auth/fb","scope":"email public_profile","response_type":"code"},"linkedIn":{"loginUrl":"https://www.linkedin.com/oauth/v2/authorization","logoutUrl":"https://api.linkedin.com/uas/oauth/invalidateToken","clientId":"e8e29n4yj1ia","redirectUri":"/auth/li","scope":"r_fullprofile r_emailaddress","response_type":"code","awliIntgCtxCode":"1035"},"linkedinCorporate":{"loginUrl":"https://www.linkedin.com/oauth/v2/authorization","logoutUrl":"https://api.linkedin.com/uas/oauth/invalidateToken","clientId":"e8e29n4yj1ia","scope":"r_fullprofile r_emailaddress","redirectUri":"/auth/li","response_type":"code","awliIntgCtxCode":"1035"}},"refineSearch":{"enabledFacets":["experience","country","state","city","category","subCategory","employmentType","requisitionRoleType","educationLevel"],"facetDisplayNames":{"experience":"Experience","country":"Country/Region","state":"State/Province ","city":"City","category":"Profession","subCategory":"Discipline","employmentType":"Employment type ","requisitionRoleType":"Role type","educationLevel":"Level of education"},"facetPlaceholderNames":{"experience":"Experience","country":"Search in country/region","state":"Search in state/province ","city":"Search in city","category":"Search in job profession","subCategory":"Search in discipline","employmentType":"Search in employment type ","requisitionRoleType":"Search in role type","educationLevel":"Search in level of education"},"defaultFacetsToOpen":["experience"]},"bundleVersions":{"msgBundle":"1","validationRules":"1"},"eagerLoadSearch":true},"recommendedTrackingConfig":{"category":{"storageKey":"categories","ddoKeysToStore":["category"],"maxKeysToStore":"4"},"job":{"storageKey":"jobsViewed","ddoKeysToStore":["jobSeqNo"],"maxKeysToStore":"4"},"search-results":[{"storageKey":"keywords","ddoKeysToStore":["keywords"],"maxKeysToStore":"4"},{"storageKey":"locations","ddoKeysToStore":["location","field"],"maxKeysToStore":"4"}]},"trackingConfig":{"ddoDataPath":{"jobDetail":"data.job"},"job_category_click":{"trait14":"key"},"similar_job_click":{"trait12":"jobSeqNo","related":{"ddo":[{"name":"jobDetail","data":{"trait5":"jobSeqNo","trait14":"category"}}]}},"linkedin_recommended_job_click":{"trait5":"jobSeqNo","trait14":"category"},"recommended_job_click":{"trait5":"jobSeqNo","trait14":"category"},"near_job_click":{"trait5":"jobSeqNo","trait14":"category"},"favorite_job_click":{"trait5":"jobSeqNo","trait14":"category"},"job_favorite_delete_click":{"trait5":"jobSeqNo","trait14":"category"},"type_ahead_search":{},"similar_job_see_more_click":{},"linkedin_login_click":{},"linkedin_logout_click":{},"view_all_glassdoor_reviews_click":{},"homepage_category_click":{"trait14":"key"},"category_click":{"trait14":"key"},"job_category_search_click":{"trait14":"key"},"job_click":{"trait5":"jobSeqNo","trait14":"category"},"previous_job_click":{"trait5":"jobSeqNo","trait14":"category"},"next_job_click":{"trait5":"jobSeqNo","trait14":"category"},"linkedin_recommended_category_click":{"trait14":"category"},"recently_viewed_job_click":{"trait5":"jobSeqNo","trait14":"category"},"back_to_search_results_click":{}},"pageNameMap":{"404":"404_page_view","home":"home_page_view","category":"job_category_page_view","featuredOpportunities":"job_category_page_view","businessUnit":"job_category_page_view","job":"job_details_view","search-results":"search_result_page_view","apply":"apply_page_view","glassdoorReviews":"glassdoor_reviews_page_view","jobcart":"favorites_page_view"}},"reqData":null},"flashParams":{},"eagerLoadRefineSearch":{"status":200,"hits":50,"totalHits":107,"data":{"jobs":[{"country":"United States","subCategory":"Business Operations & Program Management","industry":null,"title":"Senior Business Manager","multi_location":["Redmond, Washington, United States"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Redmond, Washington, United States"}],"jobSeqNo":"568231","postedDate":"2019-01-04T01:22:00","searchresults_display":null,"descriptionTeaser":"Developer Division works at the center of Microsoft strategic initiatives &ndash; building the tools and services other developers use to build software for Azure, Xbox, Windows, Mac OS, iOS, Android,","dateCreated":"2019-01-04T01:25:28.093000","state":"Washington","targetLevel":"64","jd_display":null,"reqId":null,"badge":"","jobId":"568231","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Redmond, Washington, United States","category":"Business Programs & Operations","locationLatlong":null},{"country":"India","subCategory":"Support Engineering","industry":null,"title":"Support Escalation Engineer","multi_location":["Bangalore, Karnataka, India"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Bangalore, Karnataka, India"}],"jobSeqNo":"668332","postedDate":"2019-07-15T06:15:00","searchresults_display":null,"descriptionTeaser":"Job DescriptionTo provide information and responsive and reliable resolution of the most critical and highest impact problems for Microsoft&rsquo;s strategic corporate customers using Azure App","dateCreated":"2019-07-15T06:18:36.021000","state":"Karnataka","targetLevel":"59","jd_display":null,"reqId":null,"badge":"","jobId":"668332","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Bangalore, Karnataka, India","category":"Services","locationLatlong":null},{"country":"United States","subCategory":"Program Management","industry":null,"title":"Program Manager","multi_location":["Redmond, Washington, United States"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Redmond, Washington, United States"}],"jobSeqNo":"708695","postedDate":"2019-09-20T18:34:00","searchresults_display":null,"descriptionTeaser":"LEAP Program Candidates - Are you ready for the opportunity to make a billion people more productive with software? Do you have the right skills to write and maintain services? We are looking for","dateCreated":"2019-09-20T18:36:30.777000","state":"Washington","targetLevel":"59","jd_display":null,"reqId":null,"badge":"","jobId":"708695","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Redmond, Washington, United States","category":"Engineering","locationLatlong":null},{"country":"Romania","subCategory":"Support Engineering","industry":null,"title":"Azure Database for PostgreSQL/MySQL/MariaDB Dev Support Engineer","multi_location":["Bucharest, Bucharest, Romania","Other, Other, Portugal","Other, Other, Jordan"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Bucharest, Bucharest, Romania"},{"location":"Other, Other, Portugal"},{"location":"Other, Other, Jordan"}],"jobSeqNo":"700085","postedDate":"2019-09-12T10:18:00","searchresults_display":null,"descriptionTeaser":"Role overview:Azure Database for PostgreSQL and MySQL support is a becoming a strategic unit of MicrosoftCustomer Support Services (CSS). As a Support Engineer, you will represent Microsoft in","dateCreated":"2019-09-12T10:22:37.616000","state":"Bucharest","targetLevel":"60","jd_display":null,"reqId":null,"badge":"","jobId":"700085","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Bucharest, Bucharest, Romania","category":"Services","locationLatlong":null},{"country":"India","subCategory":"Support Engineering","industry":null,"title":"Support Engineer","multi_location":["Bangalore, Karnataka, India"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Bangalore, Karnataka, India"}],"jobSeqNo":"625478","postedDate":"2019-06-30T09:10:00","searchresults_display":null,"descriptionTeaser":"Azure Database for PostgreSQL and MySQL Support Engineer Role overview: Azure Database for PostgreSQL and MySQL support is a becoming a strategic unit of Microsoft Customer Support Services (CSS). As","dateCreated":"2019-07-08T04:35:08.947000","state":"Karnataka","targetLevel":"57","jd_display":null,"reqId":null,"badge":"","jobId":"625478","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Bangalore, Karnataka, India","category":"Services","locationLatlong":null},{"country":"Costa Rica","subCategory":"Support Engineering","industry":null,"title":"Support Escalation Engineer","multi_location":["San Jose, San Jos\u00E9, Costa Rica"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"San Jose, San Jos\u00E9, Costa Rica"}],"jobSeqNo":"683146","postedDate":"2019-08-05T21:56:00","searchresults_display":null,"descriptionTeaser":"Are you interested in the cloud business and enabling Linux OSS workloads? The Microsoft Azure Platform is strategic to Microsoft enabling customers, ISVs, and Microsoft IT to develop, test, and","dateCreated":"2019-08-05T21:59:40.081000","state":"San Jos\u00E9","targetLevel":"60","jd_display":null,"reqId":null,"badge":"","jobId":"683146","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"San Jose, San Jos\u00E9, Costa Rica","category":"Services","locationLatlong":null},{"country":"Ireland","subCategory":"Inside Sales","industry":null,"title":"Sales Solution Specialist - Digital Sales. Norwegian, Finnish, Dutch, German, Danish and Swedish languages","multi_location":["Dublin, Dublin, Ireland"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Dublin, Dublin, Ireland"}],"jobSeqNo":"700066","postedDate":"2019-09-05T10:03:00","searchresults_display":null,"descriptionTeaser":"Microsoft is empowering every person and every organization on the planet to do more and achieve more. We have set ourselves three bold ambitions: create more personal computing, reinvent productivity","dateCreated":"2019-09-05T10:06:33.251000","state":"Dublin","targetLevel":"56","jd_display":null,"reqId":null,"badge":"","jobId":"700066","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Dublin, Dublin, Ireland","category":"Sales","locationLatlong":null},{"country":"United States","subCategory":"Support Engineering","industry":null,"title":"Support Escalation Engineer","multi_location":["Las Colinas, Texas, United States","Charlotte, North Carolina, United States"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Las Colinas, Texas, United States"},{"location":"Charlotte, North Carolina, United States"}],"jobSeqNo":"684810","postedDate":"2019-08-08T21:41:00","searchresults_display":null,"descriptionTeaser":"Are you interested in the cloud business and enabling Linux OSS workloads? The Microsoft Azure Platform is strategic to Microsoft enabling customers, ISVs, and Microsoft IT to develop, test, and","dateCreated":"2019-08-09T20:10:00.708000","state":"Texas","targetLevel":"62","jd_display":null,"reqId":null,"badge":"","jobId":"684810","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Las Colinas, Texas, United States","category":"Services","locationLatlong":null},{"country":"Korea","subCategory":"Support Engineering","industry":null,"title":"Support Escalation Engineer - Azure Rapid Response","multi_location":["Seoul, Seoul, Korea"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Seoul, Seoul, Korea"}],"jobSeqNo":"623537","postedDate":"2019-08-09T08:57:00","searchresults_display":null,"descriptionTeaser":"As cloud goes main stream, Azure leads the way. Azure's continued success depends on providing customers a world class support experience. Love services, support in the cloud? Customer obsessed? Data","dateCreated":"2019-08-09T09:00:32.626000","state":"Seoul","targetLevel":"58","jd_display":null,"reqId":null,"badge":"","jobId":"623537","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Seoul, Seoul, Korea","category":"Services","locationLatlong":null},{"country":"India","subCategory":"Support Engineering","industry":null,"title":"Support Escalation Engineer","multi_location":["Bangalore, Karnataka, India"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Bangalore, Karnataka, India"}],"jobSeqNo":"592315","postedDate":"2019-07-01T12:43:00","searchresults_display":null,"descriptionTeaser":"As cloud goes main stream, Azure leads the way. Azure's continued success depends on providing customers a world class support experience. Love services, support in the cloud? Customer obsessed? Data","dateCreated":"2019-07-01T12:45:09.738000","state":"Karnataka","targetLevel":"61","jd_display":null,"reqId":null,"badge":"","jobId":"592315","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Bangalore, Karnataka, India","category":"Services","locationLatlong":null},{"country":"China","subCategory":"Support Engineering","industry":null,"title":"Support Escalation Engineer_Azure Rapid Response","multi_location":["Shanghai, Shanghai, China"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Shanghai, Shanghai, China"}],"jobSeqNo":"664725","postedDate":"2019-07-17T12:55:00","searchresults_display":null,"descriptionTeaser":"&bull; As cloud goes main stream, Azure leads the way. Azure's continued success depends on providing customers a world class support experience. Love services, support in the cloud? Customer","dateCreated":"2019-07-17T12:57:31.939000","state":"Shanghai","targetLevel":"60","jd_display":null,"reqId":null,"badge":"","jobId":"664725","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Shanghai, Shanghai, China","category":"Services","locationLatlong":null},{"country":"India","subCategory":"Support Engineering","industry":null,"title":"Support Escalation Engineer","multi_location":["Hyderabad, Telangana, India"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Hyderabad, Telangana, India"}],"jobSeqNo":"701815","postedDate":"2019-09-09T11:53:00","searchresults_display":null,"descriptionTeaser":"As cloud goes main stream, Azure leads the way. Azure's continued success depends on providing customers a world class support experience. Love services, support in the cloud? Customer obsessed? Data","dateCreated":"2019-09-09T11:57:37.647000","state":"Telangana","targetLevel":"59","jd_display":null,"reqId":null,"badge":"","jobId":"701815","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Hyderabad, Telangana, India","category":"Services","locationLatlong":null},{"country":"India","subCategory":"Support Engineering","industry":null,"title":"Support Escalation Engineer","multi_location":["Hyderabad, Telangana, India"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Hyderabad, Telangana, India"}],"jobSeqNo":"690782","postedDate":"2019-08-19T08:29:00","searchresults_display":null,"descriptionTeaser":"As cloud goes main stream, Azure leads the way. Azure's continued success depends on providing customers a world class support experience. Love services, support in the cloud? Customer obsessed? Data","dateCreated":"2019-08-19T08:33:33.912000","state":"Telangana","targetLevel":"59","jd_display":null,"reqId":null,"badge":"","jobId":"690782","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Hyderabad, Telangana, India","category":"Services","locationLatlong":null},{"country":"United States","subCategory":"Software Engineering","industry":null,"title":"Senior Software Engineer","multi_location":["Redmond, Washington, United States"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Redmond, Washington, United States"}],"jobSeqNo":"653651","postedDate":"2019-06-28T18:48:00","searchresults_display":null,"descriptionTeaser":"The Linux Systems Group is looking for a talented Software Engineer to join our team. If you are interested in working on Linux or open source projects at Microsoft, this is the job for you!","dateCreated":"2019-06-28T18:51:33.424000","state":"Washington","targetLevel":"63","jd_display":null,"reqId":null,"badge":"","jobId":"653651","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Redmond, Washington, United States","category":"Engineering","locationLatlong":null},{"country":"China","subCategory":"Support Engineering","industry":null,"title":"Support Escal Eng_ARR","multi_location":["Shanghai, Shanghai, China"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Shanghai, Shanghai, China"}],"jobSeqNo":"389313","postedDate":"2018-04-11T23:30:00","searchresults_display":null,"descriptionTeaser":"As cloud goes main stream, Azure leads the way. Azure&rsquo;s continued success depends on providing customers a world class support experience. Love services, support in the cloud? Customer obsessed?","dateCreated":"2018-04-11T23:31:33.958000","state":"Shanghai","targetLevel":"60","jd_display":null,"reqId":null,"badge":"","jobId":"389313","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":1.9285714030265808,"location":"Shanghai, Shanghai, China","category":"Services","locationLatlong":null},{"country":"Romania","subCategory":"Support Engineering","industry":null,"title":"Support Escalation Engineer Azure App Services","multi_location":["Bucharest, Bucharest, Romania","Timisoara, Timis, Romania"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Bucharest, Bucharest, Romania"},{"location":"Timisoara, Timis, Romania"}],"jobSeqNo":"703831","postedDate":"2019-09-13T08:40:00","searchresults_display":null,"descriptionTeaser":"The Azure Engineer is a trusted advisor to fellow IT Professionals, using broad and in-depth troubleshooting skills and product knowledge to solve challenging technical problems. Frequently, these","dateCreated":"2019-09-13T08:51:31.215000","state":"Bucharest","targetLevel":"59","jd_display":null,"reqId":null,"badge":"","jobId":"703831","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Bucharest, Bucharest, Romania","category":"Services","locationLatlong":null},{"country":"India","subCategory":"Support Engineering","industry":null,"title":"Support Escalation Engineer","multi_location":["Hyderabad, Telangana, India"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Hyderabad, Telangana, India"}],"jobSeqNo":"704768","postedDate":"2019-09-19T12:05:00","searchresults_display":null,"descriptionTeaser":"&bull; As cloud goes main stream, Azure leads the way. Azure's continued success depends on providing customers a world class support experience. Love services, support in the cloud? Customer","dateCreated":"2019-09-19T12:08:31.561000","state":"Telangana","targetLevel":"59","jd_display":null,"reqId":null,"badge":"","jobId":"704768","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Hyderabad, Telangana, India","category":"Services","locationLatlong":null},{"country":"United States","subCategory":"Software Engineering","industry":null,"title":"Software Engineer II","multi_location":["Redmond, Washington, United States"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Redmond, Washington, United States"}],"jobSeqNo":"654470","postedDate":"2019-06-28T19:24:00","searchresults_display":null,"descriptionTeaser":"The Linux Systems Group is looking for a talented Software Engineer to join our team. If you are interested in working on Linux or open source technologies at Microsoft, this is the right team for","dateCreated":"2019-06-28T19:32:35.784000","state":"Washington","targetLevel":"62","jd_display":null,"reqId":null,"badge":"","jobId":"654470","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Redmond, Washington, United States","category":"Engineering","locationLatlong":null},{"country":"Taiwan","subCategory":"Support Engineering","industry":null,"title":"Support Escalation Engineer_Azure Rapid Response","multi_location":["Taipei, Taipei City, Taiwan"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Taipei, Taipei City, Taiwan"}],"jobSeqNo":"662515","postedDate":"2019-09-16T02:30:00","searchresults_display":null,"descriptionTeaser":"As cloud goes main stream, Azure leads the way. Azure's continued success depends on providing customers a world class support experience. Love services, support in the cloud? Customer obsessed? Data","dateCreated":"2019-09-16T02:32:33.339000","state":"Taipei City","targetLevel":"59","jd_display":null,"reqId":null,"badge":"","jobId":"662515","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Taipei, Taipei City, Taiwan","category":"Services","locationLatlong":null},{"country":"Jordan","subCategory":"Support Engineering","industry":null,"title":"Support Engineer - Azure App Services","multi_location":["Amman, Amman, Jordan"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Amman, Amman, Jordan"}],"jobSeqNo":"648261","postedDate":"2019-09-16T09:03:00","searchresults_display":null,"descriptionTeaser":" The CSS (Customer Service and Support), provides high technical service and 3rd and 4th level support for Microsoft&rsquo;s Global Enterprise and Development customers.Since the CSS (Customer Service","dateCreated":"2019-09-18T07:14:33.952000","state":"Amman","targetLevel":"59","jd_display":null,"reqId":null,"badge":"","jobId":"648261","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Amman, Amman, Jordan","category":"Services","locationLatlong":null},{"country":"Sweden","subCategory":"Customer Success Technology Solutions","industry":null,"title":"Junior Cloud Solution Architect","multi_location":["Stockholm, Stockholm, Sweden"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Stockholm, Stockholm, Sweden"}],"jobSeqNo":"700036","postedDate":"2019-09-05T08:52:00","searchresults_display":null,"descriptionTeaser":"The Opportunity: Joining the One Commercial Partner team as a Cloud Solution Architect (CSA) means you will be playing a critical role helping Microsoft Partners to capitalize on the $2.2","dateCreated":"2019-09-05T08:57:36.370000","state":"Stockholm","targetLevel":"59","jd_display":null,"reqId":null,"badge":"","jobId":"700036","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Stockholm, Stockholm, Sweden","category":"Customer Success","locationLatlong":null},{"country":"India","subCategory":"Data & Applied Sciences","industry":null,"title":"Senior Data Scientist","multi_location":["Hyderabad, Telangana, India"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Hyderabad, Telangana, India"}],"jobSeqNo":"540608","postedDate":"2018-10-29T16:36:00","searchresults_display":null,"descriptionTeaser":"Bing is a part of newly formed AI &amp; Research Organization at Microsoft. About Microsoft AI &amp; Research Org:AI &amp; Research is a new group formed at Microsoft solving to accelerate our","dateCreated":"2018-10-29T16:37:38.446000","state":"Telangana","targetLevel":"63","jd_display":null,"reqId":null,"badge":"","jobId":"540608","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":11.42795779994355,"location":"Hyderabad, Telangana, India","category":"Engineering","locationLatlong":null},{"country":"India","subCategory":"Software Engineering","industry":null,"title":"ML Engineer II","multi_location":["Hyderabad, Telangana, India"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Hyderabad, Telangana, India"}],"jobSeqNo":"463001","postedDate":"2018-07-07T03:50:00","searchresults_display":null,"descriptionTeaser":"Bing is a part of newly formed AI &amp; Research Organization at Microsoft. About Microsoft AI &amp; Research Org: AI &amp; Research is a new group formed at Microsoft solving to accelerate our","dateCreated":"2018-07-07T03:54:32.378000","state":"Telangana","targetLevel":"62","jd_display":null,"reqId":null,"badge":"","jobId":"463001","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":23.6523106069253,"location":"Hyderabad, Telangana, India","category":"Engineering","locationLatlong":null},{"country":"United States","subCategory":"Software Engineering","industry":null,"title":"Senior Developer","multi_location":["Redmond, Washington, United States"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Redmond, Washington, United States"}],"jobSeqNo":"548885","postedDate":"2019-03-13T18:43:00","searchresults_display":null,"descriptionTeaser":"The Microsoft Casual Games Studio is a small but growing team that is focused on delivering the best casual games for mobile, the web, and Windows. We have big ambitions for the future of gaming on","dateCreated":"2019-03-13T20:32:44.877000","state":"Washington","targetLevel":"63","jd_display":null,"reqId":null,"badge":"","jobId":"548885","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Redmond, Washington, United States","category":"Engineering","locationLatlong":null},{"country":"Denmark","subCategory":"Customer Success Technology Solutions","industry":null,"title":"Industry Technology Strategist (manufacturing)","multi_location":["Copenhagen, Capital Region, Denmark","Oslo, Oslo, Norway","Amsterdam, Noord-Holland, Netherlands","Vienna, Wien, Austria"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Copenhagen, Capital Region, Denmark"},{"location":"Oslo, Oslo, Norway"},{"location":"Amsterdam, Noord-Holland, Netherlands"},{"location":"Vienna, Wien, Austria"}],"jobSeqNo":"685114","postedDate":"2019-08-08T12:51:00","searchresults_display":null,"descriptionTeaser":"Microsoft is on a mission to empower every person and every organization on the planet to achieve more. Our culture iscentered on embracing a growth mindset, a theme of inspiring excellence, and","dateCreated":"2019-08-08T12:53:39.540000","state":"Capital Region","targetLevel":"62","jd_display":null,"reqId":null,"badge":"","jobId":"685114","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Copenhagen, Capital Region, Denmark","category":"Customer Success","locationLatlong":null},{"country":"Romania","subCategory":"Support Engineering","industry":null,"title":"Support Engineer (Azure App Services OSS)","multi_location":["Bucharest, Bucharest, Romania"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Bucharest, Bucharest, Romania"}],"jobSeqNo":"681349","postedDate":"2019-08-05T14:30:00","searchresults_display":null,"descriptionTeaser":"This is an external staff position. Your employer will be a third-party supplier, in service for Microsoft. The Azure Support Engineer is a trusted advisor to fellow IT Professionals, using broad and","dateCreated":"2019-08-05T14:36:34.929000","state":"Bucharest","targetLevel":"58","jd_display":null,"reqId":null,"badge":"","jobId":"681349","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Bucharest, Bucharest, Romania","category":"Services","locationLatlong":null},{"country":"Romania","subCategory":"Support Engineering","industry":null,"title":"Azure Support Escalation Engineer","multi_location":["Bucharest, Bucharest, Romania","Timisoara, Timis, Romania"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Bucharest, Bucharest, Romania"},{"location":"Timisoara, Timis, Romania"}],"jobSeqNo":"668495","postedDate":"2019-07-15T10:43:00","searchresults_display":null,"descriptionTeaser":"As cloud goes main stream, Azure leads the way. Azure&rsquo;s continued success depends on providing customers a world class support experience. Love services, support in the cloud? Customer obsessed?","dateCreated":"2019-07-15T10:45:32.689000","state":"Bucharest","targetLevel":"60","jd_display":null,"reqId":null,"badge":"","jobId":"668495","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Bucharest, Bucharest, Romania","category":"Services","locationLatlong":null},{"country":"India","subCategory":"Technical Delivery","industry":null,"title":"Consultant","multi_location":["Bangalore, Karnataka, India"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Bangalore, Karnataka, India"}],"jobSeqNo":"694402","postedDate":"2019-08-26T11:58:00","searchresults_display":null,"descriptionTeaser":"Are you ready to seize an opportunity to build leading edge technology solutions and to deploy into production with real world impact? Do you thrive by mentoring and leading by example? Would you love","dateCreated":"2019-08-26T12:02:58.161000","state":"Karnataka","targetLevel":"60","jd_display":null,"reqId":null,"badge":"","jobId":"694402","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Bangalore, Karnataka, India","category":"Services","locationLatlong":null},{"country":"United States","subCategory":"Software Engineering","industry":null,"title":"Senior Software Engineer","multi_location":["Redmond, Washington, United States"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Redmond, Washington, United States"}],"jobSeqNo":"705585","postedDate":"2019-09-16T21:15:00","searchresults_display":null,"descriptionTeaser":"The Azure Conpute - App Service team is rethinking app development for a mobile first, cloud first world. Join us now and help shape the cloud development experience of tomorrow. Azure App Service is","dateCreated":"2019-09-16T21:17:33.302000","state":"Washington","targetLevel":"63","jd_display":null,"reqId":null,"badge":"","jobId":"705585","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Redmond, Washington, United States","category":"Engineering","locationLatlong":null},{"country":"Spain","subCategory":"Support Engineering","industry":null,"title":"Azure Support Escalation Engineer","multi_location":["Madrid, Madrid, Spain"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Madrid, Madrid, Spain"}],"jobSeqNo":"686383","postedDate":"2019-09-19T08:13:00","searchresults_display":null,"descriptionTeaser":"As cloud goes mainstream, Azure leads the way. Azure&rsquo;s continued success depends on providing customers a world class support experience. Love services, support in the cloud? Customer obsessed?","dateCreated":"2019-09-19T08:15:37.813000","state":"Madrid","targetLevel":"60","jd_display":null,"reqId":null,"badge":"","jobId":"686383","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Madrid, Madrid, Spain","category":"Services","locationLatlong":null},{"country":"India","subCategory":"Support Engineering","industry":null,"title":"Support Engineer","multi_location":["Bangalore, Karnataka, India"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Bangalore, Karnataka, India"}],"jobSeqNo":"655635","postedDate":"2019-09-25T14:34:00","searchresults_display":null,"descriptionTeaser":"To provide information and reliable resolution of the most critical and highest impact problems for Microsoft&rsquo;s strategic corporate customers using IIS and ASP.NET for development and corporate","dateCreated":"2019-09-25T14:35:33.273000","state":"Karnataka","targetLevel":"58","jd_display":null,"reqId":null,"badge":"","jobId":"655635","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Bangalore, Karnataka, India","category":"Services","locationLatlong":null},{"country":"China","subCategory":"Support Engineering","industry":null,"title":"Support Escalation Engineer - Networking","multi_location":["Shanghai, Shanghai, China"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Shanghai, Shanghai, China"}],"jobSeqNo":"467978","postedDate":"2018-07-17T11:19:00","searchresults_display":null,"descriptionTeaser":"Mooncake (Azure, National Cloud in China) Support is part of CSS GCR which focuses on providing commerce, presales and technical support for Microsoft Azure across China, where Azure is one of the","dateCreated":"2018-11-16T01:48:35.451000","state":"Shanghai","targetLevel":"59","jd_display":null,"reqId":null,"badge":"","jobId":"467978","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":1.9854227303589729,"location":"Shanghai, Shanghai, China","category":"Services","locationLatlong":null},{"country":"Denmark","subCategory":"Solution Sales","industry":null,"title":"Solution Sales Specialist - Azure Application Development","multi_location":["Copenhagen, Capital Region, Denmark"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Copenhagen, Capital Region, Denmark"}],"jobSeqNo":"701802","postedDate":"2019-09-17T13:46:00","searchresults_display":null,"descriptionTeaser":"Azure is the most innovative cloud platform in computing today and Microsoft is hiring a Specialist for Azure Application Development. As a Specialist, you will be working in our enterprise sales","dateCreated":"2019-09-17T13:50:22.143000","state":"Capital Region","targetLevel":"62","jd_display":null,"reqId":null,"badge":"","jobId":"701802","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Copenhagen, Capital Region, Denmark","category":"Sales","locationLatlong":null},{"country":"Saudi Arabia","subCategory":"Business Development","industry":null,"title":"Industry Technology Strategist - Financial Services","multi_location":["Riyadh, Riyadh, Saudi Arabia"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Riyadh, Riyadh, Saudi Arabia"}],"jobSeqNo":"706564","postedDate":"2019-09-18T16:43:00","searchresults_display":null,"descriptionTeaser":"Microsoft is on a mission to empower every person and every organization on the planet to achieve more. Our culture is centered on embracing a growth mindset, a theme of inspiring excellence, and","dateCreated":"2019-09-18T16:51:42.524000","state":"Riyadh","targetLevel":"62","jd_display":null,"reqId":null,"badge":"","jobId":"706564","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Riyadh, Riyadh, Saudi Arabia","category":"Business Development & Strategy","locationLatlong":null},{"country":"Spain","subCategory":"Business Development","industry":null,"title":"Industry Technology Strategist","multi_location":["Madrid, Madrid, Spain","Other, Other, Spain","Amsterdam, Noord-Holland, Netherlands","Brussels, Brussels Region, Belgium","Luxembourg, Luxembourg, Luxembourg","Lisbon, Lisbon, Portugal","Vienna, Wien, Austria","Copenhagen, Capital Region, Denmark","Helsinki, Other, Finland","Oslo, Oslo, Norway","Stockholm, Stockholm, Sweden","Dublin, Dublin, Ireland"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Madrid, Madrid, Spain"},{"location":"Other, Other, Spain"},{"location":"Amsterdam, Noord-Holland, Netherlands"},{"location":"Brussels, Brussels Region, Belgium"},{"location":"Luxembourg, Luxembourg, Luxembourg"},{"location":"Lisbon, Lisbon, Portugal"},{"location":"Vienna, Wien, Austria"},{"location":"Copenhagen, Capital Region, Denmark"},{"location":"Helsinki, Other, Finland"},{"location":"Oslo, Oslo, Norway"},{"location":"Stockholm, Stockholm, Sweden"},{"location":"Dublin, Dublin, Ireland"}],"jobSeqNo":"712265","postedDate":"2019-09-26T18:55:00","searchresults_display":null,"descriptionTeaser":"Industries are digitally transforming and the Industry Technology Strategist (ITS) role is at the leading edge of this transformation journey with our customers. The goal of the Industry Technology","dateCreated":"2019-09-26T19:01:39.762000","state":"Madrid","targetLevel":"64","jd_display":null,"reqId":null,"badge":"","jobId":"712265","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Madrid, Madrid, Spain","category":"Business Development & Strategy","locationLatlong":null},{"country":"Ireland","subCategory":"Service Engineering","industry":null,"title":"Azure Cloud Engineer","multi_location":["Dublin, Dublin, Ireland","Other, Other, Portugal","Lisbon, Lisbon, Portugal","Other, Other, Romania","Bucharest, Bucharest, Romania","Other, Other, United Kingdom"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Dublin, Dublin, Ireland"},{"location":"Other, Other, Portugal"},{"location":"Lisbon, Lisbon, Portugal"},{"location":"Other, Other, Romania"},{"location":"Bucharest, Bucharest, Romania"},{"location":"Other, Other, United Kingdom"}],"jobSeqNo":"677401","postedDate":"2019-08-20T17:20:00","searchresults_display":null,"descriptionTeaser":"This role is based in Dublin Would you like to join one of the fastest-growing team within Microsoft Azure Engineering? Are you customer-obsessed constantly looking for enhancing customer experience?","dateCreated":"2019-08-20T17:44:34.541000","state":"Dublin","targetLevel":"62","jd_display":null,"reqId":null,"badge":"","jobId":"677401","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Dublin, Dublin, Ireland","category":"Engineering","locationLatlong":null},{"country":"United States","subCategory":"Support Engineering","industry":null,"title":"Azure Development Support Engineer","multi_location":["Las Colinas, Texas, United States","Charlotte, North Carolina, United States"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Las Colinas, Texas, United States"},{"location":"Charlotte, North Carolina, United States"}],"jobSeqNo":"643296","postedDate":"2019-06-19T21:07:00","searchresults_display":null,"descriptionTeaser":"Azure Development Support Engineer Are you interested in the cloud business? Are you motivated by customer success? The Azure PAAS Dev Support team is strategic to Microsoft enabling customers to","dateCreated":"2019-06-19T21:17:36.947000","state":"Texas","targetLevel":"60","jd_display":null,"reqId":null,"badge":"","jobId":"643296","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Las Colinas, Texas, United States","category":"Services","locationLatlong":null},{"country":"Netherlands","subCategory":"Solution Sales","industry":null,"title":"Senior Sales Specialist, Azure Application Development","multi_location":["Schiphol, Noord-Holland, Netherlands"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Schiphol, Noord-Holland, Netherlands"}],"jobSeqNo":"682242","postedDate":"2019-08-06T15:22:00","searchresults_display":null,"descriptionTeaser":"Azure is the most innovative cloud platform in computing today and Microsoft is hiring Specialist sellers for Azure Application Development. As a Specialist, you will be a senior solution sales leader","dateCreated":"2019-08-15T11:55:36.569000","state":"Noord-Holland","targetLevel":"63","jd_display":null,"reqId":null,"badge":"","jobId":"682242","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Schiphol, Noord-Holland, Netherlands","category":"Sales","locationLatlong":null},{"country":"Netherlands","subCategory":"Solution Sales","industry":null,"title":"Junior Sales Specialist, Azure Application Development","multi_location":["Schiphol, Noord-Holland, Netherlands"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Schiphol, Noord-Holland, Netherlands"}],"jobSeqNo":"682236","postedDate":"2019-08-06T15:22:00","searchresults_display":null,"descriptionTeaser":"Azure is the most innovative cloud platform in computing today and Microsoft is hiring Specialist sellers for Azure Application Development. As a Junior Sales Specialist, you will be a solution saler","dateCreated":"2019-08-15T11:55:40.902000","state":"Noord-Holland","targetLevel":"58","jd_display":null,"reqId":null,"badge":"","jobId":"682236","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Schiphol, Noord-Holland, Netherlands","category":"Sales","locationLatlong":null},{"country":"Taiwan","subCategory":"Support Engineering","industry":null,"title":"Support Engineer-Open Source Database","multi_location":["Taipei, Taipei City, Taiwan"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Taipei, Taipei City, Taiwan"}],"jobSeqNo":"680631","postedDate":"2019-08-06T08:00:00","searchresults_display":null,"descriptionTeaser":"Customer Service &amp; SupportDo you want to empower every person and every organization on the planet to achieve more?Do you want to work in an open and inclusive environment where diverse","dateCreated":"2019-08-06T08:03:43.802000","state":"Taipei City","targetLevel":"58","jd_display":null,"reqId":null,"badge":"","jobId":"680631","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Taipei, Taipei City, Taiwan","category":"Services","locationLatlong":null},{"country":"Portugal","subCategory":"Support Engineering","industry":null,"title":"Support Escalation Engineer","multi_location":["Lisbon, Lisbon, Portugal"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Lisbon, Lisbon, Portugal"}],"jobSeqNo":"639378","postedDate":"2019-06-10T15:19:00","searchresults_display":null,"descriptionTeaser":"Azure AKS Support Engineer Are you interested in the cloud business and enabling Azure Kubernetes container and OSS workloads? The Microsoft Azure Platform is strategic to Microsoft enabling","dateCreated":"2019-06-10T15:21:36.550000","state":"Lisbon","targetLevel":"61","jd_display":null,"reqId":null,"badge":"","jobId":"639378","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Lisbon, Lisbon, Portugal","category":"Services","locationLatlong":null},{"country":"United States","subCategory":"Business Strategy","industry":null,"title":"Industry Technology Strategist","multi_location":["Redmond, Washington, United States"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Redmond, Washington, United States"}],"jobSeqNo":"680930","postedDate":"2019-08-03T06:17:00","searchresults_display":null,"descriptionTeaser":"Microsoft&rsquo;s Tech for Social Impact is a full industry vertical team that works directly with nonprofits and the United Nations. The team brings together the company&rsquo;s donation and grants","dateCreated":"2019-08-03T06:19:32.593000","state":"Washington","targetLevel":"64","jd_display":null,"reqId":null,"badge":"","jobId":"680930","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Redmond, Washington, United States","category":"Business Development & Strategy","locationLatlong":null},{"country":"United States","subCategory":"Software Engineering","industry":null,"title":"Senior SAP Techno-Functional Expert","multi_location":["Issaquah, Washington, United States"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Issaquah, Washington, United States"}],"jobSeqNo":"633858","postedDate":"2019-06-03T22:20:00","searchresults_display":null,"descriptionTeaser":"Are you passionate about the customer? Would you like to solve challenging problems with a team of other brilliant engineers? Microsoft is transitioning to a cloud first world. The Business","dateCreated":"2019-06-03T22:21:39.745000","state":"Washington","targetLevel":"62","jd_display":null,"reqId":null,"badge":"","jobId":"633858","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Issaquah, Washington, United States","category":"Engineering","locationLatlong":null},{"country":"India","subCategory":"Support Engineering","industry":null,"title":"Support Escalation Engineer","multi_location":["Hyderabad, Telangana, India"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Hyderabad, Telangana, India"}],"jobSeqNo":"651691","postedDate":"2019-07-04T08:08:00","searchresults_display":null,"descriptionTeaser":"Azure AKS Support Engineer Are you interested in the cloud business and enabling Azure Kubernetes container and OSS workloads? The Microsoft Azure Platform is strategic to Microsoft enabling","dateCreated":"2019-07-04T08:11:38.173000","state":"Telangana","targetLevel":"59","jd_display":null,"reqId":null,"badge":"","jobId":"651691","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Hyderabad, Telangana, India","category":"Services","locationLatlong":null},{"country":"Ireland","subCategory":"Inside Sales","industry":null,"title":"Digital Sales Specialist \u2013 Azure - Portuguese","multi_location":["Dublin, Dublin, Ireland"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Dublin, Dublin, Ireland"}],"jobSeqNo":"686409","postedDate":"2019-08-14T20:50:00","searchresults_display":null,"descriptionTeaser":"Microsoft is empowering every person and every organization on the planet to do more and achieve more. We have set ourselves three bold ambitions: create more personal computing, reinvent productivity","dateCreated":"2019-08-14T20:56:56.764000","state":"Dublin","targetLevel":"59","jd_display":null,"reqId":null,"badge":"","jobId":"686409","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Dublin, Dublin, Ireland","category":"Sales","locationLatlong":null},{"country":"Italy","subCategory":"Customer Success Technology Solutions","industry":null,"title":"Cloud Solution Architect","multi_location":["Rome, Roma, Italy"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Rome, Roma, Italy"}],"jobSeqNo":"676174","postedDate":"2019-09-02T09:38:00","searchresults_display":null,"descriptionTeaser":"We are looking for a highly motivated and passionate Cloud Solution Architect for Cloud Applications and Infrastructure solutions to drive high priority customer initiatives on the Microsoft Azure","dateCreated":"2019-09-12T13:16:33.785000","state":"Roma","targetLevel":"61","jd_display":null,"reqId":null,"badge":"","jobId":"676174","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Rome, Roma, Italy","category":"Customer Success","locationLatlong":null},{"country":"China","subCategory":"Support Engineering","industry":null,"title":"Support Escalation Engineer_Azure Kubernetes&Bare Metal","multi_location":["Shanghai, Shanghai, China","Wuxi, Jiangsu, China"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Shanghai, Shanghai, China"},{"location":"Wuxi, Jiangsu, China"}],"jobSeqNo":"660254","postedDate":"2019-08-06T00:25:00","searchresults_display":null,"descriptionTeaser":"Are you interested in the cloud business and enabling Azure Kubernetes container and OSS workloads? The Microsoft Azure Platform is strategic to Microsoft enabling customers, ISVs, and Microsoft IT to","dateCreated":"2019-08-28T02:38:34.006000","state":"Shanghai","targetLevel":"58","jd_display":null,"reqId":null,"badge":"","jobId":"660254","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Shanghai, Shanghai, China","category":"Services","locationLatlong":null},{"country":"Ireland","subCategory":"Inside Tech Sales","industry":null,"title":"Digital Cloud Solution Architect, Azure - Italian speaker","multi_location":["Dublin, Dublin, Ireland"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Dublin, Dublin, Ireland"}],"jobSeqNo":"702782","postedDate":"2019-09-11T11:50:00","searchresults_display":null,"descriptionTeaser":"Microsoft is empowering every person and every organization on the planet to do more and achieve more. We have set ourselves three bold ambitions: create more personal computing, reinvent productivity","dateCreated":"2019-09-11T11:52:45.297000","state":"Dublin","targetLevel":"59","jd_display":null,"reqId":null,"badge":"","jobId":"702782","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Dublin, Dublin, Ireland","category":"Technical Sales","locationLatlong":null},{"country":"United States","subCategory":"Support Engineering","industry":null,"title":"Support Escalation Engineer - Azure Kubernetes Services","multi_location":["Charlotte, North Carolina, United States"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Charlotte, North Carolina, United States"}],"jobSeqNo":"676787","postedDate":"2019-08-03T06:30:00","searchresults_display":null,"descriptionTeaser":"Support Escalation Engineer - Azure Kubernetes Services Are you interested in the cloud business and enabling Azure Kubernetes container and OSS workloads? The Microsoft Azure Platform is strategic to","dateCreated":"2019-08-03T06:31:37.554000","state":"North Carolina","targetLevel":"62","jd_display":null,"reqId":null,"badge":"","jobId":"676787","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Charlotte, North Carolina, United States","category":"Services","locationLatlong":null},{"country":"India","subCategory":"Support Engineering","industry":null,"title":"Support Engineer","multi_location":["Bangalore, Karnataka, India"],"type":null,"orgFunction":null,"experience":"Experienced professionals","locale":"en_us","multi_location_array":[{"location":"Bangalore, Karnataka, India"}],"jobSeqNo":"697656","postedDate":"2019-09-13T09:25:00","searchresults_display":null,"descriptionTeaser":"Azure App Services - Support Engineer Are you interested in working on a technology that is on Microsoft&rsquo;s top priorities? Are you passionate about working on emerging technologies and shaping","dateCreated":"2019-09-13T09:35:01.335000","state":"Karnataka","targetLevel":"57","jd_display":null,"reqId":null,"badge":"","jobId":"697656","isMultiLocation":true,"jobVisibility":["external"],"mostpopular":0.0,"location":"Bangalore, Karnataka, India","category":"Services","locationLatlong":null}],"aggregations":[{"field":"country","value":{"United States":24,"India":18,"Ireland":16,"Romania":8,"China":7,"Portugal":5,"Australia":4,"Costa Rica":4,"Netherlands":4,"Sweden":4,"Denmark":3,"Japan":3,"Korea":3,"Spain":3,"Austria":2,"Italy":2,"Jordan":2,"Norway":2,"Taiwan":2,"United Kingdom":2,"Belgium":1,"Finland":1,"Hong Kong SAR":1,"Israel":1,"Luxembourg":1,"Saudi Arabia":1,"Singapore":1,"South Africa":1}},{"field":"subCategory","value":{"Support Engineering":43,"Customer Success Technology Solutions":16,"Inside Tech Sales":12,"Solution Sales":10,"Software Engineering":7,"Inside Sales":6,"Technology Solutions":4,"Business Development":2,"Technical Delivery":2,"Business Operations & Program Management":1,"Business Strategy":1,"Data & Applied Sciences":1,"Program Management":1,"Service Engineering":1}},{"field":"educationLevel","value":{"Bachelors":6,"None":5}},{"field":"employmentType","value":{"Full-Time":105,"Temp/Contract":2}},{"field":"city","value":{"Dublin":16,"Hyderabad":9,"Bucharest":8,"Bangalore":7,"Other":7,"Redmond":7,"Shanghai":6,"Las Colinas":5,"Lisbon":4,"New York":4,"San Jose":4,"Sydney":4,"Charlotte":3,"Copenhagen":3,"Madrid":3,"Seoul":3,"Stockholm":3,"Tokyo":3,"Amsterdam":2,"Oslo":2,"Schiphol":2,"Taipei":2,"Timisoara":2,"Vienna":2,"Alpharetta":1,"Amman":1,"Austin":1,"Beijing":1,"Bentonville":1,"Brussels":1,"Chicago":1,"Cyberport":1,"Dallas":1,"Durban":1,"Fargo":1,"Gothenburg":1,"Gurgaon":1,"Helsinki":1,"Herzliya":1,"Issaquah":1,"Luxembourg":1,"Mumbai":1,"Reading":1,"Reston":1,"Riyadh":1,"Rome":1,"Singapore (APAC-HQ)":1,"Sunnyvale":1,"Wuxi":1}},{"field":"state","value":{"Dublin":16,"Telangana":9,"Bucharest":8,"Other":8,"Washington":8,"Karnataka":7,"Texas":7,"Shanghai":6,"Lisbon":4,"New South Wales":4,"New York":4,"Noord-Holland":4,"San Jos\u00E9":4,"Capital Region":3,"Madrid":3,"North Carolina":3,"Seoul":3,"Stockholm":3,"Tokyo-to":3,"Oslo":2,"Taipei City":2,"Timis":2,"Wien":2,"Amman":1,"Arkansas":1,"Beijing":1,"Berkshire":1,"Brussels Region":1,"California":1,"Georgia":1,"Haryana":1,"Illinois":1,"Jiangsu":1,"KwaZulu-Natal":1,"Luxembourg":1,"Maharashtra":1,"North Dakota":1,"Riyadh":1,"Roma":1,"Tel Aviv":1,"Virginia":1,"V\u00E4stra G\u00F6taland":1}},{"field":"category","value":{"Services":45,"Customer Success":16,"Sales":16,"Technical Sales":16,"Engineering":10,"Business Development & Strategy":3,"Business Programs & Operations":1}},{"field":"experience","value":{"Experienced professionals":107}},{"field":"requisitionRoleType","value":{"Individual Contributor":107}}],"locationData":{"place_id":"","latitude":"","longitude":"","aboveMaxRadius":"true","placeVal":""},"searchConfig":{"mostpopular":true}},"eid":"5d8f42dfab1f9e4eb179adad"}}; phApp.sessionParams = {"csrfToken":"ba3e9a1cbf8b4833a2d43c3dc7dc7425","pageType":"default","keywords":"php","jdsource":"","from":"0","pageName":"search-results"}; /*-->*/ </script><script type="text/javascript">document.domain = 'phenompeople.com'</script><script type="text/javascript">phApp.urlMap = {"featuredOpportunities":":url", "businessUnit":":url", "category": "c/:category","job": "job/:jobSeqNo/:title","glassdoor-reviews": "glassdoor-reviews", "search-results" : "search-results", "home" : "home", "jobcart" : "jobcart"}  </script><script type="text/javascript">phApp.ddoRealPath = {"jobDetail": "data.job"}</script><script type="text/javascript" src="https://prodcmscdn.azureedge.net/careerconnectresources/p/common/js/ph-tracking.js?v=1"> </script><script type="text/javascript" src="https://prodcmscdn.azureedge.net/careerconnectresources/p/common/js/appConfig/ph-app-config-1.2.js?v=1"> </script><meta charset="UTF-8"><meta content="en"><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"><meta name="description" content="Search results. Find available job openings at Microsoft" key-description="default-search-results-description"><meta name="keywords" content="job search results, ${keywords}" key-keywords="default-search-results-keywords"><meta name="twitter:card" content="summary"><meta name="twitter:site" content="@Microsoft"><meta name="twitter:creator" content="@Careers - Microsoft"><meta name="twitter:image" content="https://prodcmscdn.azureedge.net/careerconnectresources/p/MICRUS/social/Share_msft-1526988101412.jpg"><meta name="twitter:title" content="Search results  | Find available job openings at Microsoft"><meta name="twitter:description" content="Search results. Find available job openings at Microsoft"><meta property="og:type" content="website"><meta property="og:image" content="https://prodcmscdn.azureedge.net/careerconnectresources/p/MICRUS/social/Share_msft-1526996096885.jpg"><meta property="og:site_name" content="Microsoft"><meta property="og:url" content="https://careers.microsoft.com/us/en/search-results"><meta property="og:title" content="Search results  | Find available job openings at Microsoft"><meta property="og:description" content="Search results. Find available job openings at Microsoft"><meta property="fb:admins" content=""><meta property="og:image:width" content="200"><meta property="og:image:height" content="200"><title data-ph-id="ph-page-element-page19-X7A0Fi" key="default-search-results-title">Search results  | Find available job openings at Microsoft</title><script type="text/x-ph-tmpl" id="ph-oauthsignin-v1-1559835047040-my-profile">
#                                     <button role="button" aria-label="Right side overflow scroll" key-aria-label="z5b0az-parent-jt9mae-ph-oauthsignin-v1-my-profile-showNextMenuOptionsLabelText" class="nav-arrow-right show-arrow" onclick="ph$Msft$Custom.header_overFlow_menu_right()" data-ph-id="ph-page-element-short-header-z5b0az-y2fvAD">
#                                         <i class="icon icon-arrow-right" aria-hidden="true" data-ph-id="ph-page-element-short-header-z5b0az-7CCtjP"></i>
#                                     </button>
#                                     <span if.bind="user.isLoggedIn === false" data-ph-id="ph-page-element-short-header-z5b0az-lnyOMs">
#                                         <button role="button" id="sign-profile" onfocus="ph$Msft$Custom.header_mainAnchors_onFocus(this);ph$Msft$Custom.header_signinAnchor_onFocus();" ph-tevent="signIn_click" click.delegate="handlePagePath($event, 'login')" aria-label="Sign in" class="btn primary-button" key-aria-label="z5b0az-parent-jt9mae-ph-oauthsignin-v1-my-profile-careersSignInLinkLabelText" data-ph-id="ph-page-element-short-header-z5b0az-pI3nJq">
#                                             <p data-ph-id="ph-page-element-short-header-z5b0az-d27CFv"><ppc-content key="z5b0az-parent-jt9mae-ph-oauthsignin-v1-my-profile-careersSignInLinkText" data-ph-id="ph-page-element-short-header-z5b0az-GaDFa0">Sign in</ppc-content></p>
#                                         </button>
#                                     </span>
#                                     <span class="profile-container" if.bind="user.isLoggedIn === true" data-ph-at-id="profile-info" data-ph-at-firstname-text="${user.profile.firstName}" data-ph-at-lastname-text="${user.profile.lastName}" data-ph-at-userrole-text="${user.profile.headline}" data-ph-at-userlocation-text="${user.profile.location}" data-ph-id="ph-page-element-short-header-z5b0az-iIyElP">
#                                         <button role="button" if.bind="user.profile.preferredFirstName" aria-label="Hi, ${user.profile.preferredFirstName}" onclick="ph$Msft$Custom.login_User_Details_Menu(this)" aria-expanded="false" title="Hi, ${user.profile.preferredFirstName}" class="btn primary-button profile-title" onfocus="ph$Msft$Custom.header_userDetails_Menu_onFocus(this)" id="user-name" data-ph-id="ph-page-element-short-header-z5b0az-3M6J1q">
#                                             <p data-ph-id="ph-page-element-short-header-z5b0az-kOpC4p"><span class="hiLabel" data-ph-id="ph-page-element-short-header-z5b0az-riuStK">
#                                                 <ppc-content key="z5b0az-parent-jt9mae-ph-oauthsignin-v1-my-profile-headerxboxLinkText1" data-ph-at-id="linkedin-recommended-jobs-profile-hello-text" data-ph-id="ph-page-element-short-header-z5b0az-b2tHkU">Hi,</ppc-content>
#                                             </span>
#                                             <span class="userName" data-ph-id="ph-page-element-short-header-z5b0az-53IIi5"> ${user.profile.preferredFirstName}!</span></p>
#                                             <i class="icon icon-down-arrow header-arrow" aria-hidden="true" data-ph-id="ph-page-element-short-header-z5b0az-EgPc18"></i>
#                                         </button>
#                                         <button role="button" if.bind="!user.profile.preferredFirstName || user.profile.preferredFirstName == ''" aria-label="Hi, ${user.profile.firstName}" title="Hi, ${user.profile.firstName}" onclick="ph$Msft$Custom.login_User_Details_Menu(this)" aria-expanded="false" class="btn primary-button profile-title" onfocus="ph$Msft$Custom.header_userDetails_Menu_onFocus(this)" id="user-name" data-ph-id="ph-page-element-short-header-z5b0az-Lm5hib">
#                                             <p data-ph-id="ph-page-element-short-header-z5b0az-STV198"><span class="hiLabel" data-ph-id="ph-page-element-short-header-z5b0az-Uh08j2">
#                                                 <ppc-content key="z5b0az-parent-jt9mae-ph-oauthsignin-v1-my-profile-headerxboxLinkText1" data-ph-at-id="linkedin-recommended-jobs-profile-hello-text" data-ph-id="ph-page-element-short-header-z5b0az-FDZ0nM">Hi,</ppc-content>
#                                             </span>
#                                             <span class="userName" data-ph-id="ph-page-element-short-header-z5b0az-lax5B5"> ${user.profile.firstName}!</span></p>
#                                             <i class="icon icon-down-arrow header-arrow" aria-hidden="true" data-ph-id="ph-page-element-short-header-z5b0az-vomGRp"></i>
#                                         </button>
#                                         <ul class="menupanel" aria-labelledby="user-name" id="candidate-details" data-ph-at-id="loggedin-actions" data-ph-id="ph-page-element-short-header-z5b0az-MHUT6o">
#                                             <li data-ph-id="ph-page-element-short-header-z5b0az-P1kcBa">
#                                                 <a ph-tevent="header_menu_click" key-ph-href="z5b0az-parent-jt9mae-ph-oauthsignin-v1-my-profile-careersProfileLinkUrl" data-ph-tevent-attr-trait62="Profile" class="menu-item secondheader-nav" role="link" ph-href="/us/en/profile" aria-label="Profile" key-aria-label="z5b0az-parent-jt9mae-ph-oauthsignin-v1-my-profile-careersProfileLinkLabelText" data-ph-at-id="profile-link" data-ph-id="ph-page-element-short-header-z5b0az-pTSCRg">
#                                                     <ppc-content key="z5b0az-parent-jt9mae-ph-oauthsignin-v1-my-profile-careersProfileLinkText" data-ph-at-id="profile-text" data-ph-id="ph-page-element-short-header-z5b0az-hkuEAS">Profile</ppc-content>
#                                                 </a>
#                                             </li>
#                                             <li data-ph-id="ph-page-element-short-header-z5b0az-2yOUpm">
#                                                 <a ph-href="/us/en/managejobalerts" key-ph-href="z5b0az-parent-jt9mae-ph-oauthsignin-v1-my-profile-jobAlertsNavTextUrl" class="menu-item secondheader-nav" aria-label="Job alerts" key-aria-label="z5b0az-parent-jt9mae-ph-oauthsignin-v1-my-profile-jobAlertsNavLabelText" ph-tevent="header_menu_click" data-ph-tevent-attr-trait62="Job alerts" role="link" data-ph-at-id="jobalerts-link" data-ph-id="ph-page-element-short-header-z5b0az-XZ4CYr">
#                                                     <ppc-content key="z5b0az-parent-jt9mae-ph-oauthsignin-v1-my-profile-jobAlertsNavText" data-ph-at-id="jobalerts-text" data-ph-id="ph-page-element-short-header-z5b0az-8MmTqT">Job alerts</ppc-content>
#                                                 </a>
#                                             </li>
#                                             <li data-ph-id="ph-page-element-short-header-z5b0az-PfzbY8">
#                                                 <a ph-tevent="header_menu_click" data-ph-tevent-attr-trait62="Action center" class="menu-item secondheader-nav" role="link" ph-href="/us/en/actioncenter" key-ph-href="z5b0az-parent-jt9mae-ph-oauthsignin-v1-my-profile-headerActionCenterLinkUrl" aria-label="Action center" key-aria-label="z5b0az-parent-jt9mae-ph-oauthsignin-v1-my-profile-actioncenterLinktext" data-ph-at-id="action-center-link" data-ph-id="ph-page-element-short-header-z5b0az-7r9tfT">
#                                                     <ppc-content key="z5b0az-parent-jt9mae-ph-oauthsignin-v1-my-profile-headerActionCenterLinkText" data-ph-at-id="action-center-text" data-ph-id="ph-page-element-short-header-z5b0az-YWTp9o">Action center</ppc-content>
#                                                 </a>
#                                             </li>
#                                             <li data-ph-id="ph-page-element-short-header-z5b0az-SGVJVI">
#                                                 <a ph-tevent="logout_click" ph-href="logout?qpage=%2Fus%2Fen%2F&amp;page=home" aria-label="Sign out from Microsoft careers" role="link" key-aria-label="z5b0az-parent-jt9mae-ph-oauthsignin-v1-my-profile-signOutLinkLabeltext" data-ph-at-id="logout-link" data-ph-id="ph-page-element-short-header-z5b0az-JxKmXI">
#                                                     <span class="action-content-title" data-ph-id="ph-page-element-short-header-z5b0az-Zlpv4F">
#                                                         <ppc-content key="z5b0az-parent-jt9mae-ph-oauthsignin-v1-my-profile-signOutLinktext" data-ph-at-id="logout-text" data-ph-id="ph-page-element-short-header-z5b0az-4H87af">Sign out</ppc-content>
#                                                     </span>
#                                                 </a>
#                                             </li>
#                                         </ul>
#                                     </span>
#                                 </script><script type="text/x-ph-tmpl" id="ph-job-cart-count-v3-1559835047050-view1">
#                                     <a ph-href="/us/en/savedjobs" key-ph-href="u6t44s-parent-jt9mae-ph-job-cart-count-v3-view1-careersSavedJobsLinkUrl" class="phs-job-cart-area" ph-tevent="job-cart-icon-click" aria-label="Saved jobs ${jobCartCount > 0 ? jobCartCount : ''}" onfocus="ph$Msft$Custom.header_mainAnchors_onFocus(this)" tip-suggestion="Saved jobs" data-ph-at-id="jobcart-count" data-ph-at-widget-data-count="${jobCartCount}" data-ph-id="ph-page-element-short-header-u6t44s-bqZC0I">
#                                         <ppc-content type="icon" data-ph-id="ph-page-element-short-header-u6t44s-gOoRzb">
#                                             <i class="${jobCartCount > 0? 'icon icon-star' : 'icon icon-star-empty'}" aria-hidden="true" data-ph-id="ph-page-element-short-header-u6t44s-ShS36W"></i>
#                                         </ppc-content>
#                                         <span class="savedJobsText" data-ph-id="ph-page-element-short-header-u6t44s-R993qp">
#                                             <ppc-content key="u6t44s-parent-jt9mae-ph-job-cart-count-v3-view1-careersSavedJobsLinkText" data-ph-at-id="heading-text" data-ph-id="ph-page-element-short-header-u6t44s-aHSv3w">Saved jobs</ppc-content>
#                                         </span>
#                                         <span class="${jobCartCount > 0 ? 'phs-jobcart-count' : 'phs-jobcart-count hide'}" key="u6t44s-parent-jt9mae-ph-job-cart-count-v3-view1-${jobCartCount}LinkText" data-ph-id="ph-page-element-short-header-u6t44s-2lQHXe">${jobCartCount}</span>
#                                     </a>
#                                 </script><script type="text/x-ph-tmpl" id="ph-create-job-alert-v1-46yred-default">
#    <div class="phs-create-job-alert-area ph-widget-box" if.bind="isLoggedIn === true" data-ph-id="ph-page-element-page19-dHzFoh">
#     <div class="ph-create-job-alert-block" role="region" aria-labelledby="create_alert" data-ph-id="ph-page-element-page19-FCkZjA">
#      <div class="heading-block" data-ph-id="ph-page-element-page19-Jkbr6h">
#       <div class="heading-area ph-a11y-create-alert-submit" tabindex="-1" aria-label="Job alerts" data-ph-id="ph-page-element-page19-gzltDE">
#        <h2 id="create_alert" data-ph-id="ph-page-element-page19-EYMNMp">
#         <ppc-content key="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertText" data-ph-at-id="heading-text" data-ph-id="ph-page-element-page19-Y5XETn">
#           Create job alert
#         </ppc-content> </h2>
#        <p if.bind="showSuccessMsg === true" data-ph-id="ph-page-element-page19-WryRVt"> <a aria-label="view your job alerts" key-aria-label="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertLinkAriaLabelText" ph-href="/us/en/managejobalerts" key-ph-href="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertPhhrefLinkGlobalUrl" data-ph-id="ph-page-element-page19-Uf4tD3"> <span data-ph-id="ph-page-element-page19-l4gm81">
#           <ppc-content key="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertLinkText" data-ph-id="ph-page-element-page19-xiVhLp">
#             View your job alerts
#           </ppc-content> </span> </a> </p>
#       </div>
#      </div>
#      <!-- Consolidated error block for this section Start -->
#      <div class="error-message-wrapper ${ hasErrors ? 'padding-alert':''}" data-ph-id="ph-page-element-page19-Gi1gLw">
#       <div class="alert-form-message" aria-live="assertive" aria-atomic="true" data-ph-id="ph-page-element-page19-tKfoKa">
#        <!-- <button class="close-error" aria-label="Close this error message" click.delegate="_closeErrorBlock('errors')" role="button" type="button">
#                                                     <i class="icon icon-cancel" aria-hidden="true"></i>
#                                                 </button>                                                     -->
#        <div class="error-title" if.bind="hasErrors &amp;&amp; errors.name == 'E104'" data-ph-id="ph-page-element-page19-jJQAiO">
#         <ppc-content key="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertSelectSearchCriteriaText" data-ph-id="ph-page-element-page19-S1qtxg">
#          You have no search criteria selected. Please enter at least one keyword or search filter above to create a job alert.
#         </ppc-content>
#        </div>
#       </div>
#       <div class="alert-form-message" aria-live="assertive" aria-atomic="true" data-ph-id="ph-page-element-page19-76y6Es">
#        <!-- <button class="close-error" aria-label="Close this error message" click.delegate="_closeErrorBlock('errors')" role="button" type="button">
#                                                     <i class="icon icon-cancel" aria-hidden="true"></i>
#                                                 </button>                                                     -->
#        <div class="error-title" if.bind="hasErrors &amp;&amp; errors.name == 'E105'" data-ph-id="ph-page-element-page19-26jer9">
#         <ppc-content key="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertDuplicateText" data-ph-id="ph-page-element-page19-58g29K">
#          Duplicate alert criteria
#         </ppc-content>
#        </div>
#       </div>
#       <div class="alert-form-message" aria-live="assertive" aria-atomic="true" data-ph-id="ph-page-element-page19-DLPCz1">
#        <!-- <button class="close-error" aria-label="Close this error message" click.delegate="_closeErrorBlock('errors')" role="button" type="button">
#                                                     <i class="icon icon-cancel" aria-hidden="true"></i>
#                                                 </button>                                                     -->
#        <div class="error-title" if.bind="hasErrors &amp;&amp; errors.name == 'E400'" data-ph-id="ph-page-element-page19-rzxE60">
#         ${errors.message}
#        </div>
#       </div>
#       <div class="alert-form-message" aria-live="assertive" aria-atomic="true" data-ph-id="ph-page-element-page19-YX3qiZ">
#        <!-- <button class="close-error" aria-label="Close this error message" click.delegate="_closeErrorBlock('errors')" role="button" type="button">
#                                                     <i class="icon icon-cancel" aria-hidden="true"></i>
#                                                 </button>                                                     -->
#        <div class="error-title" if.bind="hasErrors &amp;&amp; errors.name == 'E404'" data-ph-id="ph-page-element-page19-3XCVk6">
#         <ppc-content key="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertOppsErrorText" data-ph-id="ph-page-element-page19-73DZ9P">
#          Oops! An error occurred. Please try again
#         </ppc-content>
#        </div>
#       </div>
#      </div>
#      <!-- Consolidated error block for this section End -->
#      <!-- Job alerts create section start -->
#      <div class="job-alert-create-area" if.bind="showSuccessMsg === false &amp;&amp; errors.name != 'E106'" data-ph-id="ph-page-element-page19-FqxEtL">
#       <div class="sub-heading" data-ph-id="ph-page-element-page19-3h0ZRD">
#        <ppc-content key="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertInformationsText" data-ph-at-id="sub-heading-text" data-ph-id="ph-page-element-page19-3ZgUxr">
#         Receive daily, weekly or monthly emails with jobs matching your search criteria or select the email frequency as none if you'd only like to save this search.
#        </ppc-content>
#       </div>
#       <div class="create-form-fields-block" data-ph-id="ph-page-element-page19-NyiInH">
#        <form role="form" action="" submit.delegate="validateOnAlertCreation(event, alertName)" data-ph-id="ph-page-element-page19-LSjCkJ">
#         <div class="row form-group" data-ph-id="ph-page-element-page19-sKQEkM">
#          <div class="col-xs-12 col-md-10 form-field" data-ph-id="ph-page-element-page19-IleQ29">
#           <label for="firstname" data-ph-id="ph-page-element-page19-VhEZOc">
#            <ppc-content key="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertAlertNameText" data-ph-id="ph-page-element-page19-Wz4En7">
#             Alert name
#            </ppc-content> </label>
#           <input type="text" ref="alertName" id="firstname" name="name" class.bind="hasErrors &amp;&amp; errors.name == 'E103'?'error-block':''" value.bind="createJobAlertModel.name" blur.trigger="validateName()" autocomplete="off" aria-required="true" aria-invalid="${hasErrors &amp;&amp; errors.name == 'E103'?'true':'false'}" aria-label="Enter job alert name" key-aria-label="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertAlertNameAriaLabelText" placeholder="Enter alert name" key-placeholder="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertAlertNamePlaceHolderText" data-ph-id="ph-page-element-page19-OP06zG">
#            <div class="announce-error-block" aria-atomic="true" aria-live="polite" data-ph-id="ph-page-element-page19-vpYop2">
#             <span class="error error-active" if.bind="hasErrors &amp;&amp; errors.name == 'E103'" data-ph-id="ph-page-element-page19-Nty4fe">
#              <ppc-content key="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertAlertNameErrorReqText" data-ph-id="ph-page-element-page19-rroWbW">
#                Alert name is required
#              </ppc-content> </span>
#            </div> </input>
#          </div>
#         </div>
#         <div class="row form-group" data-ph-id="ph-page-element-page19-MI8lJu">
#          <div class="col-xs-12 form-field" data-ph-id="ph-page-element-page19-m95Zsk">
#           <label for="frequency_name" class="email-freq" data-ph-id="ph-page-element-page19-mXZgD6">
#            <ppc-content key="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertEmalText" data-ph-id="ph-page-element-page19-dT26PX">
#             I'd like to get emails
#            </ppc-content> </label>
#           <div class="custom-select-group" data-ph-id="ph-page-element-page19-XpUO2J">
#            <span class="custom-dropdown-arrow" data-ph-id="ph-page-element-page19-6w2FQU"> <i class="icon icon-down-arrow" aria-hidden="true" data-ph-id="ph-page-element-page19-AS7ZN1"></i> </span>
#            <select autocomplete="off" id="frequency_name" name="frequency" value.bind="createJobAlertModel.frequency" aria-label="Select email frequency" key-aria-label="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertEmalFreqSelectAriaLabelText" data-ph-id="ph-page-element-page19-FPfZ3h"> <option repeat.for="data of masterFrequency" value="${data.key}" data-ph-id="ph-page-element-page19-gTptLm">${data.frequency}</option> </select>
#           </div>
#          </div>
#         </div>
#         <div class="row form-group" data-ph-id="ph-page-element-page19-jV0jMO">
#          <div class="col-xs-12 col-md-10 form-field" data-ph-id="ph-page-element-page19-3rFFYj">
#           <button type="submit" role="button" class="btn btn-primary" aria-label="Create job alert" key-aria-label="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertCreateAlertBtnAriaLabelText" data-ph-id="ph-page-element-page19-VNJ5S3">
#            <ppc-content key="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertCreateAlertBtnText" data-ph-id="ph-page-element-page19-0XlRKQ">
#             Create job alert
#            </ppc-content> </button>
#          </div>
#         </div>
#        </form>
#       </div>
#       <div class="bottom-block note-block" data-ph-id="ph-page-element-page19-5gCBuO">
#        <p data-ph-id="ph-page-element-page19-CJvRaH"> <span data-ph-id="ph-page-element-page19-KhodmS">
#          <ppc-content key="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertCreatingNoticeText1" data-ph-id="ph-page-element-page19-LGzagK">
#           Notice: By creating this alert, you consent to receiving communication about job opportunities based on the search criteria specified and the email you provided during the authentication to the Microsoft Careers Site. You can opt out from receiving these emails at any time via the
#          </ppc-content> </span> <a ph-href="/us/en/managejobalerts" key-ph-href="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertManageAlertsPhhrefLinkGlobalUrl" aria-label="job alerts" key-aria-label="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertManageAlertsLinkAriaLabelText" data-ph-id="ph-page-element-page19-oDk7Jd"> <span data-ph-id="ph-page-element-page19-D7RcMd">
#           <ppc-content key="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertManageAlertsLinkText" data-ph-id="ph-page-element-page19-uLyJ15">
#            job alerts
#           </ppc-content> </span> </a> <span data-ph-id="ph-page-element-page19-8iqiiH">
#          <ppc-content key="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertCreatingNoticeText2" data-ph-id="ph-page-element-page19-g1Wgen">
#           page
#          </ppc-content> </span> </p>
#       </div>
#      </div>
#      <!-- Job alerts create section end -->
#      <!-- max limit information section start -->
#      <div if.bind="hasErrors &amp;&amp; errors.name == 'E106'" class="max-limit-info" data-ph-id="ph-page-element-page19-MbvJDW">
#       <p data-ph-id="ph-page-element-page19-zy9zPb"> <i class="icon icon-warning" aria-hidden="true" data-ph-id="ph-page-element-page19-RDT1YA"></i> <span data-ph-id="ph-page-element-page19-0xOmGE">
#         <ppc-content key="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertReachedMaxAmountText1" data-ph-id="ph-page-element-page19-80UuAU">
#          You have reached the limit of 10 job alerts. You can remove existing alerts on the
#         </ppc-content> </span> <a aria-label="job alerts" key-aria-label="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertReachedMaxAmountManageLinkAriaLabelText" ph-href="/us/en/managejobalerts" key-ph-href="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertReachedMaxAmountManagePhhrefLinkGlobalUrl" data-ph-id="ph-page-element-page19-cl1HHU"> <span data-ph-id="ph-page-element-page19-1cQP23">
#          <ppc-content key="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertReachedMaxAmountManageLinkText" data-ph-id="ph-page-element-page19-NsYn96">
#           job alerts
#          </ppc-content> </span> </a> <span data-ph-id="ph-page-element-page19-cGo04Y">
#         <ppc-content key="46yred-ph-create-job-alert-v1-default-headingLevel2createJobAlertReachedMaxAmountText2" data-ph-id="ph-page-element-page19-r3v7RN">
#          page.
#         </ppc-content> </span> </p>
#      </div>
#      <!-- <a aria-label="view your job alerts" ph-href="managejobalerts"></a> -->
#      <!-- max limit information section End -->
#      <!-- Job alerts success section start -->
#      <div class="job-alert-success-area" aria-live="assertive" aria-atomic="true" data-ph-id="ph-page-element-page19-JSKg6N">
#       <div class="success-container" if.bind="showSuccessMsg === true &amp;&amp; errors.name != 'E106'" data-ph-id="ph-page-element-page19-umMbXx">
#        <div class="success-heading-block" data-ph-id="ph-page-element-page19-WPIGjy">
#         <div class="success-heading-area" data-ph-id="ph-page-element-page19-A77av8">
#          <h3 data-ph-id="ph-page-element-page19-p7TcHg"> <i class="ms-icon msicon-fullmdl2assets-32" aria-hidden="true" data-ph-id="ph-page-element-page19-7nFrZS"></i> <span data-ph-id="ph-page-element-page19-LI5zs5">
#            <ppc-content key="46yred-ph-create-job-alert-v1-default-headingLevel2Hl3createJobAlertCreatedSucFulText" data-ph-id="ph-page-element-page19-OyYN1s">
#             Job alert created successfully
#            </ppc-content> </span> </h3>
#         </div>
#        </div>
#        <div class="user-alert-data-block" data-ph-id="ph-page-element-page19-rplGzo">
#         <div class="alert-info-block" data-ph-id="ph-page-element-page19-ziG4U9">
#          <label data-ph-id="ph-page-element-page19-BVfRTk">
#           <ppc-content key="46yred-ph-create-job-alert-v1-default-headingLevel2Hl3createJobAlertCreatedSucFulNameText" data-ph-id="ph-page-element-page19-RjDk1i">
#            Alert name:
#           </ppc-content> </label>
#          <span data-ph-id="ph-page-element-page19-j3D5FX">${createJobAlertModel.name}</span>
#         </div>
#         <div class="alert-info-block" data-ph-id="ph-page-element-page19-HjWwZX">
#          <label data-ph-id="ph-page-element-page19-TYyTuh">
#           <ppc-content key="46yred-ph-create-job-alert-v1-default-headingLevel2Hl3createJobAlertCreatedSucFulEmailText" data-ph-id="ph-page-element-page19-yz6E3F">
#            You will get emails:
#           </ppc-content> </label>
#          <span data-ph-id="ph-page-element-page19-DqtU2B">${getFrequencyObject(createJobAlertModel.frequency).frequency}</span>
#         </div>
#        </div>
#        <div class="success-bottom-block" data-ph-id="ph-page-element-page19-8y4TCR">
#         <!-- <p>
#                                                         <ppc-content key="tipTexttocreateNewoneText">To create a new alert, modify the search criteria. </ppc-content>
#                                                     </p> -->
#         <button type="submit" role="button" class="btn btn-primary" aria-label="Create new job alert" key-aria-label="46yred-ph-create-job-alert-v1-default-headingLevel2Hl3createJobAlertCreatedSucFulNewAlertBtnAriaLabelText" click.delegate="createNewAlert()" data-ph-id="ph-page-element-page19-CXPPbS">
#          <ppc-content key="46yred-ph-create-job-alert-v1-default-headingLevel2Hl3createJobAlertCreatedSucFulNewAlertBtnText" data-ph-id="ph-page-element-page19-CjKxmh">
#           Create new job alert
#          </ppc-content> </button>
#        </div>
#       </div>
#      </div>
#      <!-- Job alerts success section end -->
#     </div>
#    </div> </script><script type="text/x-ph-tmpl" id="ph-language-selector-v1-1564397942232-language-link">
#                                     <div ph-loading-img="show-loader.bind: showLoader" show.bind="showLoader" class="show-loader" data-ph-id="ph-page-element-footer-eqfhjt-fQJ8Me"></div>
#                                     <div class="phs-lang-select-area ph-widget-box" show.bind="!showLoader" data-ph-id="ph-page-element-footer-eqfhjt-wBx3MK">
#                                         <div class="phs-lang-select-list" data-ph-id="ph-page-element-footer-eqfhjt-rgR2q5">
#                                             <ul data-ph-id="ph-page-element-footer-eqfhjt-X0KzyG">
#                                                 <li repeat.for="lang of supportedLanguages" data-ph-id="ph-page-element-footer-eqfhjt-KK3YeB">
#                                                     <a href="javascript:void(0)" class="${chosenLanguage.locale == lang.locale ? 'active' : ''}" click.delegate="languageChanged(lang)" aria-label="Redirects to ${lang.description} Version of Site" data-ph-id="ph-page-element-footer-eqfhjt-JQav0j">
#                                                         <img ph-src="assets/images/${lang.locale}.png" alt="${lang.description} icon" aria-hidden="true" data-ph-id="ph-page-element-footer-eqfhjt-WYUiM2">
#                                                         <span data-ph-id="ph-page-element-footer-eqfhjt-sUIiQL">${lang.locale.split('_')[0].toUpperCase()}</span>
#                                                     </img></a>
#                                                 </li>
#                                             </ul>
#                                         </div>
#                                     </div>
#                                 </script><script type="text/x-ph-tmpl" id="ph-search-results-v1-view-external-1565777110191">
#
#                                 <!-- <span class="sr-only" aria-live="assertive" aria-hidden="true" aria-atomic="true" innerhtml="${isDataUpdated ? 'Showing '+startingJobNumberInPage+' to '+endingJobNumberInpage+ ' of '+ totalJobs + createdAlertName +' jobs' : ''}"></span> -->
#
#                                 <div class="phs-facet-results-block" role="region" aria-label="Search results block" key-aria-label="2fssdu-ph-search-results-v1-view-external-srRegionBlockAriaLabelText" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-2gJFYk">
#                                     <div class="show-loader" ph-loading-img="show-loader.bind: showLoader" show.bind="showLoader" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-E6fPuu"></div>
#                                     <div class="phs-results-actions" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-E4WXyi">
#                                         <!--Header part for search results-->
#                                         <div class="phs-jobs-list-header row" data-ph-at-id="jobs-list-header" data-ph-at-search-keyword-text="${searchKeyword}" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-YOneBz">
#                                             <!-- Result count block -->
#                                             <div id="content" aria-live="assertive" aria-atomic="true" class="col-xs-8" data-ph-at-starting-job-number-text="${startingJobNumberInPage}" data-ph-at-ending-job-number-text="${endingJobNumberInpage}" data-ph-at-total-jobs-text="${totalJobs}" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-nki5yM">
#                                                 <div if.bind="!showLoader &amp;&amp; totalJobs" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-6B1ulD">
#                                                     <span if.bind="totalJobs > 0" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Z8kD3k">
#                                                         <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultText" data-ph-at-id="showing-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5ou0Pc">
#           Showing
#         </ppc-content>
#                                                         <span class="job-number" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-RdIQRR"> ${startingJobNumberInPage} </span>
#                                                         <span class="job-number" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-I5vvvg">
#                                                             <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultHyphenText" data-ph-at-id="hyphen-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-T2wITv">
#            -
#          </ppc-content>
#                                                         </span>
#                                                         <span class="sr-only" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Hw2vPe"><ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultToText" data-ph-at-id="to-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-UPlP8x">
#           to
#          </ppc-content></span>
#                                                         <span class="job-number" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-p6nkOz"> ${endingJobNumberInpage} </span>
#                                                         <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultOfText" data-ph-at-id="of-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-iQfvpC">
#           of
#         </ppc-content>
#                                                     </span>
#                                                     <span class="total-jobs" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-m0Utvg"> ${totalJobs} </span>
#                                                     <span if.bind="!searchKeyword &amp;&amp; !createdAlertName" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-k1n8GN">
#                                                         <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultjobsText" data-ph-at-id="countLabel" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-vRelI8">
#          jobs
#         </ppc-content>
#                                                     </span>
#                                                     <span if.bind="searchKeyword || createdAlertName" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-9b58l8">
#                                                         <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultResText" data-ph-at-id="results-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-uYhx5J">
#          results
#         </ppc-content>
#                                                     </span>
#                                                     <span if.bind="searchKeyword || createdAlertName" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Z9NTA6">
#                                                         <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultForText" data-ph-at-id="for-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-O8Z3mV">
#          for
#         </ppc-content>
#                                                     </span>
#                                                     <span if.bind="searchKeyword &amp;&amp; !createdAlertName" class="search-keyword" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-trD4PI">${searchKeyword}</span>
#                                                     <span if.bind="createdAlertName" class="search-keyword" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-BJLR8O">${createdAlertName}</span>
#                                                 </div>
#                                             </div>
#                                             <!--End Result count block -->
#                                             <div class="col-xs-4" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-1bVDI4">
#                                                 <div class="remove-padding" if.bind="!showLoader &amp;&amp; totalJobs" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Wia4kL">
#                                                     <div class="pull-right phs-header-controls" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Y89J9E">
#                                                         <!-- Filter block hidden mode-->
#                                                         <div tabindex="0" class="phs-jobs-list-count" show.bind="totalJobs > 0" aria-label="${totalJobs} jobs" data-ph-at-id="search-page-top-job-count" data-ph-at-count="${totalJobs}" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-hrbnzX">
#                                                             ${totalJobs}
#                                                             <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultForJobsPluralText" data-ph-at-id="countLabel" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CyOWBa">
#            jobs
#           </ppc-content>
#                                                         </div>
#                                                         <div class="phs-filter" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-WHQsVH">
#                                                             <a href="javascript:void(0)" click.delegate="showFacetFilter()" aria-label="Filter button" key-aria-label="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultFilterAriaLabelText" data-ph-at-id="mobile-facet-filter-menu-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-WNeBYS">
#                                                                 <ppc-content type="icon" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-efY17s">
#                                                                     <i class="icon icon-filter" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-aEWA2L"></i>
#                                                                 </ppc-content>
#                                                             </a>
#                                                         </div>
#                                                         <!--End Filter block -->
#
#                                                         <!-- sort jobs block -->
#                                                         <div class="phs-jobs-list-sort phs-taglib" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-clNZVf">
#                                                             <label for="sortselect" class="control-label" data-ph-at-id="sortby-label" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-raRQki">
#                                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSortJobsText" data-ph-at-id="sortby-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-8v2Zsx">
#             Sort by
#            </ppc-content>
#                                                             </label>
#                                                             <div class="sortby" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-pFhfla">
#                                                                 <select id="sortselect" aria-label="Sort by" key-aria-label="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSortJobsAriaLabelText" class="form-control" value.bind="searchParams.sortBy" change.delegate="sortfilterSearch($event)" data-ph-at-id="sortby-drop-down" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-mxiPkX">
#                                                                     <option value="Most relevant" key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSortJobsOptions1" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-P5ywOC">Most relevant</option>
#                                                                     <option value="Most recent" key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSortJobsOptions2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-dg5AHq">Most recent</option>
#                                                                     <option value="Most popular" if.bind="isMostPopular" key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSortJobsOptions3" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-PhOKut">Most popular</option>
#                                                                 </select>
#                                                                 <i class="icon icon-down-arrow" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ccUqwU"></i>
#                                                             </div>
#                                                         </div>
#                                                          <!--End sort jobs block -->
#                                                     </div>
#                                                 </div>
#                                             </div>
#                                         </div>
#                                         <!--End Header part for search results-->
#
#                                         <!--Selected Facet Tags-->
#                                         <ul class="phs-facet-tags" data-ph-at-id="facet-tags-list" if.bind="searchSelectionKeys.length > 0 || (searchKeyword &amp;&amp; isLoggedIn)" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-WxdYKi">
#                                             <li class="tag" repeat.for="selection of searchSelectionKeys" if.bind="searchSelectionKeys.length > 0" data-ph-at-id="facet-tags-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5WGud3">
#                                                 <div class="selected-lable" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CQXvDZ">
#                                                       <span class="facet-tag" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Vz8d1X">${selection.name}</span>
#                                                       <a href="javascript:void(0)" click.delegate="clearSelection(selection)" role="button" key-role="TOjxeN-2fssdu-ph-search-results-v1-view-external-btnRole" aria-label="Remove ${selection.name}" data-ph-at-id="tag-${selection.facet}-link" data-ph-at-text="${selection.name}" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-DWExX8">
#                                                          <ppc-content type="icon" data-ph-at-id="tag-${selection.facet}-close-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-dA7X1N">
#                                                         <i class="icon icon-cancel" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ejGyso"></i>
#                                                        </ppc-content>
#                                                      </a>
#                                                 </div>
#                                             </li>
#                                             <li class="phs-facet-tags-clear" if.bind="searchSelectionKeys.length > 0" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-tL7Cy8">
#                                             <div class="selected-lable" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-NGtKpa">
#                                                 <a class="clearall" href="javascript:void(0)" click.delegate="emptySelectionsAndCallSearch()" ph-tevent="clear_searches_click" role="button" key-role="7RUTz4-2fssdu-ph-search-results-v1-view-external-btnRole" aria-label="Clear all selected filters in refine your search section" key-aria-label="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultClearAllSFAriaLabelText" data-ph-at-id="clear-all-facet-tags-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-lGup4h">
#                                                     <span data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-QXe2Ly"><ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultClearAllSelectionText" data-ph-at-id="clear-all-facet-tags-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-zjjlRZ">
#           Clear all
#          </ppc-content></span>
#                                                 </a>
#                                             </div>
#                                             </li>
#                                             <li class="phs-facet-tags-clear" if.bind="(isLoggedIn &amp;&amp; searchSelectionKeys.length > 0) || (isLoggedIn &amp;&amp; searchKeyword)" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-knxR5Y">
#                                                 <div class="selected-lable" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-GESVVy">
#                                                 <a class="create-alert" href="#create_alert" data-ph-at-id="create-job-alert-facet-tags-link" aria-label="Create job alert" key-aria-label="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultCreateJobAlertAriaLabelText" role="link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-fm9wuR">
#                                                     <span data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-rorpd6"><ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultCreateJobAlertText" data-ph-at-id="create-job-alert-facet-tags-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-BTfigP">
#           Create job alert
#          </ppc-content></span>
#                                                 </a>
#                                                 </div>
#                                             </li>
#                                         </ul>
#                                         <!--End Seleceted Facet Tags-->
#                                     </div>
#                                     <div show.bind="!showLoader &amp;&amp; totalJobs" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-hI3iJF">
#                                         <!--Facet results-->
#                                         <div class="phs-jobs-list" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-1E6CFC">
#                                             <div class="phs-jobs-block" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-xd06Qs">
#                                                 <ul data-ph-at-id="jobs-list" data-ph-at-widget-data-count="${jobResults.length}" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-a2DVXy">
#                                                     <li class="jobs-list-item" repeat.for="eachResult of jobResults" data-ph-at-id="jobs-list-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-y4hTr0">
#                                                         <div class="information-block row" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-zEw2pE">
#                                                             <div class="left-block col-xs-12 col-md-10" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-rmeHWW">
#                                                                 <!-- jobs link block -->
#                                                                 <div class="information" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-fm9Dgs">
#                                                                     <a focus.bind="$index == 0 &amp;&amp; currentSelectedPage > 1" ph-tevent="job_click" ref="linkEle" href="${getUrl(linkEle, 'job', eachResult)}" role="link" key-role="2fssdu-ph-search-results-v1-view-external-linkRole" aria-label="${eachResult.title} job ID ${eachResult.jobSeqNo} opens in a new tab" target="_blank" data-ph-at-id="job-link" data-ph-at-job-title-text="${eachResult.title}" data-ph-at-job-location-text="${eachResult.location}" data-ph-at-job-category-text="${eachResult.category}" data-ph-at-job-id-text="${eachResult.jobId}" data-ph-at-job-type-text="${eachResult.type}" data-ph-at-job-industry-text="${eachResult.industry}" data-ph-at-job-post-date-text="${eachResult.postedDate}" data-ph-at-job-seqno-text="${eachResult.jobSeqNo}" data-ph-at-job-position-text="${eachResult.positionLevel}" data-ph-at-job-employment-type-text="${eachResult.employmentType}" data-ph-at-job-role-type-text="${eachResult.requisitionRoleType}" data-ph-at-job-education-level-text="${eachResult.educationLevel}" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ic7VNu">
#                                                                         <span class="job-title" data-ph-at-id="searchresults-job-title" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-MRnq6A">${eachResult.title}</span>
#                                                                     </a>
#                                                                     <div class="job-additional-info" data-ph-at-id="job-info" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LesJKv">
#                                                                         <span class="job-location" if.bind="eachResult.multi_location.length == 1 &amp;&amp; eachResult.multi_location[0]" data-ph-at-id="searchresults-job-location" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CQMOUl">
#                                                                             ${eachResult.multi_location[0]}
#                                                                         </span>
#                                                                         <span class="job-category" if.bind="eachResult.category" data-ph-at-id="searchresults-job-category" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-g94YTa">
#                                                                             ${eachResult.category}
#                                                                         </span>
#                                                                         <span class="job-date" aria-label="${eachResult.postedDate | dateFormat:getDateFormat('DEFAULT')}" if.bind="eachResult.postedDate" data-ph-at-id="searchresults-job-postdate" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-b6UGw3">
#                                                                             ${eachResult.postedDate | dateFormat:"MMM D, YYYY"}
#                                                                         </span>
#                                                                     </div>
#                                                                     <div class="description" innerhtml.bind="eachResult.descriptionTeaser | sanitizeHTML" data-ph-at-id="jobdescription-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Abw08f"></div>
#                                                                 </div>
#                                                                 <!--End jobs link block -->
#
#                                                                 <!-- jobs multilocation block -->
#                                                                 <div class="job-multi-locations" if.bind="eachResult.multi_location.length > 1" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-vJOVzG">
#                                                                     <button ph-tevent="multi_location_click" data-ph-tevent-attr-trait14="${eachResult.category}" data-ph-tevent-attr-trait5="${eachResult.jobSeqNo}" keyup.trigger="($event.keyCode === 27)?(eachResult.toggleOpen = false):''" class="esc$$close" click.delegate="eachResult.toggleOpen = !eachResult.toggleOpen" role="button" key-role="IWwth6-2fssdu-ph-search-results-v1-view-external-btnRole" id="searchLoc-${$index}" aria-expanded="${eachResult.toggleOpen ? 'true' : 'false'}" aria-label="${eachResult.title} job ID ${eachResult.jobSeqNo} Job available in ${eachResult.multi_location.length} locations" data-ph-at-id="job-multi-locations-button" data-ph-at-job-multilocation-count="${eachResult.multi_location.length}" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0aUp1e">
#                                                                         <span data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-h6pjaT"><ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultJobAvailText1" data-ph-at-id="multilocation-text1" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5DjjWH">
#               Job available in
#              </ppc-content></span> ${eachResult.multi_location.length} <span data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5Lm1HA"><ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultJobAvailText2" data-ph-at-id="multilocation-text2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-2Go8OT">
#               locations
#              </ppc-content></span>
#                                                                         <!--icon toggle based on item click: js dependent-->
#                                                                         <!--<i ref="listItemIcon" class="icon icon-down-arrow" aria-hidden="true"></i>-->
#                                                                         <i ref="listItemIcon" class="${eachResult.toggleOpen ? 'icon icon-up-arrow' : 'icon icon-down-arrow'}" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-KotPHt"></i>
#                                                                     </button>
#                                                                     <!--dropView used to toggle toggleMultiLocationView based on item click: js dependent-->
#                                                                     <ul ref="listItem" aria-hidden="${eachResult.toggleOpen ? 'false' : 'true'}" class="${eachResult.toggleOpen ? 'show' : 'hide'}" data-ph-at-id="job-multi-locations-list" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-cbms8u">
#                                                                         <li class="location" repeat.for="eachLocation of eachResult.multi_location" aria-label="${eachLocation}" data-ph-at-id="job-multi-location-item" data-ph-at-job-location-text="${eachLocation}" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-EgsS0Q">
#                                                                             ${eachLocation}
#                                                                         </li>
#                                                                     </ul>
#                                                                 </div>
#                                                                 <!--End jobs multilocation block -->
#                                                             </div>
#                                                             <div class="right-block col-xs-12 col-md-2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-W9vvx1">
#                                                                 <!-- Job applied status block -->
#                                                                 <div class="applied-action" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0WA3mP">
#                                                                     <section class="ph-widget" instance-id="we3alx" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CGkAfP" view="1565777110184-default" original-view="default" theme="default">
#                                                                         <div as-element="ph-job-status-v1" arrjoblist.bind="$index===0 ? jobResults : null" jobid="${eachResult.jobSeqNo}" view="1565777110184-default" mode="APPLY" class="ph-job-status-v1-default-default ph-widget-target" data-widget="ph-job-status-v1" instance-id="we3alx" original-view="default" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TWsAYD"></div>
#                                                                     </section>
#                                                                 </div>
#                                                                 <!--End Job applied status block -->
#
#                                                                 <!-- Job saved block -->
#                                                                 <div class="actions" data-ph-at-id="job-actions" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Kt42DX">
#                                                                     <!--<div as-element="ph-add-to-cart-v1" if.bind="!bulkcart" data-widget="ph-add-to-cart-v1" job-detail.bind="eachResult" class="ph-add-to-cart-v1-default-default" view="view1"></div>-->
#                                                                     <div class="savejob-checkbox" if.bind="bulkcart" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-lWmxkg">
#                                                                         <label class="${eachResult.inProgress ? 'disabled' : ''}" for="save-${eachResult.jobSeqNo}-${$index}" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-eySiqX">
#                                                                             <input type="checkbox" id="save-${eachResult.jobSeqNo}-${$index}" checked.bind="eachResult.isJobSaved" change.delegate="handleSaveJob(eachResult)" aria-label="Save ${eachResult.title} job ID ${eachResult.jobSeqNo} to job cart" aria-checked="${eachResult.isJobSaved ? 'true' : 'false'}" role="checkbox" data-ph-at-id="save-click" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LoOray">
#                                                                             <span class="label-content" if.bind="eachResult.isJobSaved === false" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5iZTnr">
#                                                                                 <i class="icon icon-star-empty" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-3hSiPg"></i>
#                                                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSaveText" data-ph-at-id="save-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-V3uiSa">
#                 Save
#                </ppc-content>
#                                                                             </span>
#                                                                             <span class="label-content" if.bind="eachResult.isJobSaved === true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-OFLjjD">
#                                                                                 <i class="icon icon-star" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-WCVb2F"></i>
#                                                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSavedText" data-ph-at-id="save-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-2rXAWz">
#                 Saved
#                </ppc-content>
#                                                                             </span>
#                                                                         </input></label>
#                                                                     </div>
#                                                                 </div>
#                                                                  <!--End Job saved block -->
#                                                             </div>
#                                                         </div>
#                                                     </li>
#                                                 </ul>
#                                             </div>
#                                         </div>
#                                         <!--End Facet results-->
#                                         <!--Bottom Result count block -->
#                                         <div class="pagination-block" show.bind="paginationRange.length > 1" data-ph-at-id="pagination-block" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-NqUtB4">
#                                             <div class="search-bottom-count" data-ph-at-id="pagination-info" data-ph-at-starting-job-number-text="${startingJobNumberInPage}" data-ph-at-ending-job-number-text="${endingJobNumberInpage}" data-ph-at-total-jobs-text="${totalJobs}" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-WzXjXE">
#                                                 <span if.bind="totalJobs > 0" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-A0f9qa">
#                                                     <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultPaginationText" data-ph-at-id="showing-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-7ZTFG1"> Showing </ppc-content>
#                                                     <span class="job-number" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-v3eF8w"> ${startingJobNumberInPage} </span>
#                                                     <span class="job-number" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Ks6MAG">
#                                                         <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResulttPaginationHyphenText" data-ph-at-id="hyphen-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-rgOn5T"> - </ppc-content>
#                                                     </span>
#                                                     <span class="sr-only" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-H5FW4P"><ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResulttPaginationToText" data-ph-at-id="to-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-hX5Etf">to</ppc-content></span>
#                                                     <span class="job-number" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-wRvYTe"> ${endingJobNumberInpage} </span>
#                                                     <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResulttPaginationOfText" data-ph-at-id="of-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-y4CzyC"> of</ppc-content>
#                                                 </span>
#                                                 <span class="total-jobs" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-k8yAFK"> ${totalJobs} </span>
#                                                 <span if.bind="!searchKeyword &amp;&amp; !createdAlertName" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-uruH1i">
#                                                     <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResulttPaginationjobsText" data-ph-at-id="countLabel" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Tqrfl0">jobs</ppc-content>
#                                                 </span>
#                                                 <span if.bind="searchKeyword || createdAlertName" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-R5DwsU">
#                                                     <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResulttPaginationResText" data-ph-at-id="results-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-NPnFds">results</ppc-content>
#                                                 </span>
#                                                 <span if.bind="searchKeyword || createdAlertName" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-lbxlHZ">
#                                                     <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResulttPaginationForText" data-ph-at-id="for-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-6xu68J">for</ppc-content>
#                                                 </span>
#                                                 <span if.bind="searchKeyword &amp;&amp; !createdAlertName" class="search-keyword" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-HxZYsR">${searchKeyword}</span>
#                                                 <span if.bind="createdAlertName" class="search-keyword" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-K8ReUY">${createdAlertName}</span>
#                                             </div>
#                                             <!--End Bottom Result count block -->
#
#                                             <!-- Bottom Pagination block -->
#                                             <div role="region" aria-label="pagination block" key-aria-label="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultPaginationBlockAriaLabelText" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-MgIi4Z">
#                                                 <ul class="pagination" data-ph-at-id="pagination" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-eaRwzq">
#                                                     <li data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-NzMW9r">
#                                                         <a href.bind="paginationUrl(currentSelectedPage - 1)" aria-label="View previous page" key-aria-label="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultBottomPrevAriaLabelText" show.bind="prevButtonVisibility" ph-tevent="pagination_click" data-ph-tevent-attr-trait214="Previous" role="button" key-role="Ufch4m-2fssdu-ph-search-results-v1-view-external-btnRole" data-ph-at-id="pagination-previous-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-tb6U4s">
#                                                             <ppc-content type="icon" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-wmx9c7">
#                                                                 <span aria-hidden="true" class="icon icon-left-arrow" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-YGmDzY"></span>
#                                                             </ppc-content>
#                                                             <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultBottomPrevText" data-ph-at-id="pagination-previous-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-aTG1pH">
#            Prev
#          </ppc-content>
#                                                         </a>
#                                                     </li>
#                                                     <li repeat.for="page of paginationRange" class="${currentSelectedPage == page ? 'active' : ''}" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TTJEHU">
#                                                         <a href.bind="paginationUrl(page)" onclick="getElementById('eachJob').focus()" ph-tevent="pagination_click" data-ph-tevent-attr-trait214="${page}" role="button" aria-label="${currentSelectedPage == page ? 'current ' : ''}page ${page}" key-aria-label="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultPaginationDynamicAriaLabelText" data-ph-at-id="pagination-page-number-link" data-ph-at-text="${page}" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ms3YtQ">${page}</a>
#                                                     </li>
#                                                     <li data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-D7fLOK">
#                                                         <a href.bind="paginationUrl(currentSelectedPage + 1)" aria-label="View Next page" key-aria-label="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultBottomNextAriaLabelText" show.bind="nextButtonVisibility" ph-tevent="pagination_click" data-ph-tevent-attr-trait214="Next" role="button" key-role="oMJpEz-2fssdu-ph-search-results-v1-view-external-btnRole" data-ph-at-id="pagination-next-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-hclKdV">
#                                                             <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultBottomNextText" data-ph-at-id="pagination-next-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-wXm0qV">
#            Next
#          </ppc-content>
#                                                             <ppc-content type="icon" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-StE6iW">
#                                                                 <span aria-hidden="true" class="icon icon-arrow-right" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Jqai1g"></span>
#                                                             </ppc-content>
#                                                         </a>
#                                                     </li>
#                                                 </ul>
#                                             </div>
#                                             <!--End Bottom Pagination block -->
#                                         </div>
#                                     </div>
#                                     <!-- No jobs Found block-->
#                                     <div class="phs-nojobs-found-category" if.bind="!totalJobs &amp;&amp; !showLoader" aria-live="assertive" role="alert" aria-atomic="true" aria-labelledby="noResults" data-ph-at-id="nodata-block" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-3Z1gE5">
#                                         <!--Nojobs Found text area-->
#                                         <div class="no-result-info" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-QFRDhc">
#                                             <p id="noResults" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-KeALR2">
#                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultNoJobsText" data-ph-at-id="nodata-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-NhX6ZX">
#          We could not find any matching jobs.
#        </ppc-content>
#                                             </p>
#                                         </div>
#                                         <!--End Nojobs Found text area-->
#                                     </div>
#                                     <!--End Nojobs Found block-->
#                                 </div>
#                             </script><script type="text/x-ph-tmpl" id="ph-job-status-v1-1565777110184-default">
#                                                                             <div class="applied-block" if.bind="isApplied === true" data-ph-id="ph-default-ph-job-status-v124sCBa">
#                                                                                 <!-- <img src="../assets/images/Check-mark.png" key-src="searchResultsShowingResultAppliedBtnImgSrc" alt="" key-alt="searchResultsShowingResultAppliedBtnImgAltText" aria-hidden="true"> -->
#                                                                                 <span class="sr-only" data-ph-id="ph-default-ph-job-status-v1RBQ5Tx"><ppc-content key="we3alx-ph-job-status-v1-default-searchResultsExtShowingResultAppliedOfScreenTextText" data-ph-id="ph-default-ph-job-status-v1u0zeO3">
#       Job status :
#      </ppc-content></span>
#                                                                                 <i class="icon icon-check-mark" aria-hidden="true" data-ph-id="ph-default-ph-job-status-v19Hfp6r"></i>
#                                                                                 <span data-ph-id="ph-default-ph-job-status-v1WRE8gh"><ppc-content key="we3alx-ph-job-status-v1-default-searchResultsExtShowingResultAppliedText" data-ph-id="ph-default-ph-job-status-v1EYRjgD">
#       Applied
#      </ppc-content></span>
#                                                                             </div>
#                                                                         </script><script type="text/x-ph-tmpl" id="ph-global-search-v3-default-1566408052426">
#                                     <form class="phs-global-search-area ph-widget-box" aria-label="Find jobs" key-aria-label="p3mrzw-ph-global-search-v3-default-homeGlobalsearchFormAriaLabel" keyup.delegate="arrowKeyUp($event)" novalidate="" action="" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-fdlAOn">
#                                         <div class="search-text-block" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-Ajdiqe">
#                                             <!-- <h1 if.bind="showTitle">
#                                                 <ppc-content key="homeGlobalsearchHeading1doWhatYouLoveText" data-ph-at-id="widget-heading-text">Do what you love</ppc-content>
#                                             </h1> -->
#                                             <!-- <p if.bind="showCaption">
#                                                 <ppc-content key="searchJobsHeading">Search jobs</ppc-content>
#                                             </p>                                         -->
#                                         </div>
#                                         <!-- <div class="short-ratio-btn-group">
#                                             <p>
#                                                 <ppc-content key="chooseOpportunityText">Opportunity type:</ppc-content>
#                                             </p>
#                                             <div class="raio-btn-block">
#                                                 <label class="inpu-radio-group">
#                                                     <input type="radio" value="professional" checked.bind="selectedReqType" name="experiencedreqtype" id="professional_radio" aria-label="Experienced professionals">
#                                                     <span class="radio-seletced"></span>
#                                                     <span class="radio-text">
#                                                         <ppc-content key="homeGlobalsearchHeading1ProfessionalLabelText">Experienced
#                                                             professionals</ppc-content>
#                                                     </span>
#                                                 </label>
#                                             </div>
#                                             <div class="raio-btn-block">
#                                                 <label class="inpu-radio-group">
#                                                     <input type="radio" value="university" checked.bind="selectedReqType" name="studentsreqtype" id="university_radio" aria-label="Students and recent graduates">
#                                                     <span class="radio-seletced"></span>
#                                                     <span class="radio-text">
#                                                         <ppc-content key="homeGlobalsearchHeading1StudentsLabelText">Students
#                                                             and recent graduates</ppc-content>
#                                                     </span>
#                                                 </label>
#                                             </div>
#                                         </div> -->
#                                         <div class="form-group" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-PYXVY7">
#                                             <div class="input-group row" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-4YN3jm">
#                                                 <div class="col-xs-10" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-WJdU9r">
#                                                     <div class="job-filter ph-suggestion-focus-block" data-ph-at-id="keyword-category-location" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-0QtpB2">
#                                                         <input id="searchBox" type="text" name="phsKeywords" focus.trigger="handleFocus($event)" blur.trigger="gsClrTxt = 0" key-placeholder="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeadingPlaceholderText" ref="phGSearchInput" aria-label="Search jobs" key-aria-label="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeadingSearchLinkAriaLabelText" onkeydown="arrowacce$$List(event)" placeholder="Search jobs" class="form-control phs-keywords input-lg" value.bind="searchValue &amp; debounce:100" maxlength="200" autocomplete="off" data-ph-at-id="globalsearch-input" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-Jr4Lqz">
#                                                         <span class="search-sym" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-uUs5bF">
#                                                             <ppc-content type="icon" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-gTGRWv">
#                                                                 <i class="icon icon-search" aria-hidden="true" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-ZOvdLi"></i>
#                                                             </ppc-content>
#                                                         </span>
#                                                         <div class="clear-block" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-Ck6tyj">
#                                                             <button data-ph-at-id="clear-globalsearch-link" type="button" keyup.trigger="gsClrTxt = 1" mouseup.trigger="gsClrTxt = 1" ph-tevent="clear_searches_click" class="phs-keysearch-clear" role="button" click.trigger="clearSearch($event)" onclick="setTimeout(function(){document.getElementById('searchBox').focus(); gsClrTxt = 0},500)" show.bind="searchValue" href="javascript:void(0)" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-l5RzZA">
#                                                                 <ppc-content type="icon" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-wNgHsj">
#                                                                     <i class="icon icon-cancel" aria-hidden="true" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-VxD3sn"></i>
#                                                                 </ppc-content>
#                                                                 <span class="sr-only" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-eC1C0E">
#                                                                     <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1OffScreenReaderClearText" data-ph-at-id="clear-globalsearch-text" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-AYQLrZ">
#            Clear text
#           </ppc-content>
#                                                                 </span>
#                                                             </button>
#                                                         </div>
#                                                         <div class="phs-search-suggestions${showDropDown ? ' search-visible':''}" if.bind="showDropDown" id="searchSuggest" aria-label="Search suggestions" key-aria-label="p3mrzw-ph-global-search-v3-default-homeGSHeadingLevel1SearchOpenBlockAriaLabelText" role="region" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-qdGlO5">
#                                                             <div class="phs-search-type-ahead phs-onclick-category" if.bind="showAllJobCategories" data-ph-at-id="onclick-category" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-Vz0cDS">
#                                                                 <div class="phs-search-categories" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-uFEsZa">
#                                                                     <h3 data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-NCbvXA">
#                                                                         <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1HL3ProfessionsText" data-ph-at-id="heading-text" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-kKktk8">
#              Professions
#             </ppc-content>
#                                                                     </h3>
#                                                                     <ul class="phs-search-category-list" repeat.for="categoryColumns of allJobCategories" data-ph-at-id="category-list" data-ph-at-total-data-count="${allJobCategories.length}" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-zy1dcX">
#                                                                         <li repeat.for="category of categoryColumns" class="job-search-keyblock job-container-category_${$parent.$index}_${$index}" data-ph-at-id="category-list-item" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-X0JGQn">
#                                                                             <a ph-tevent="job_category_search_click" id="phs-lia_${$parent.$index}_${$index}" ref="linkEle" data-presentation-title="${category.key}" href.bind="getUrl(linkEle, 'category', category)" role="link" data-ph-at-id="category-link" data-ph-at-data-text="${category.key}" data-ph-at-data-count="${category.total_count}" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-W8YIM8">
#                                                                                 <span class="phs-${category.key}" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-r0oKcm">${category.key}</span>
#                                                                                 <span class="phs-jobs-count phs-${category.total_count}" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-j7AhNq">${category.total_count}</span>
#                                                                                 <span class="sr-only" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-5FXiGO">
#                                                                                     <span if.bind="category.total_count == 1" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-uKhdT9">
#                                                                                         <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1HL3CatogeryJobText" data-ph-at-id="countLabel" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-ikpAee">
#                  job
#                 </ppc-content>
#                                                                                     </span>
#                                                                                     <span if.bind="category.total_count > 1" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-E2Dff2">
#                                                                                         <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1HL3CatogeryJobsText" data-ph-at-id="countLabel" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-VpW8o5">
#                  jobs
#                 </ppc-content>
#                                                                                     </span>
#                                                                                 </span>
#                                                                             </a>
#                                                                         </li>
#                                                                     </ul>
#                                                                 </div>
#                                                             </div>
#                                                             <div class="phs-keyword-suggestions" if.bind="showJobSuggestions &amp;&amp; searchValue.length >= 3" aria-label="Job Suggestions" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-tkQE1n">
#                                                                 <!--Location-->
#                                                                 <!--TODO: for city, state, country property name dependent on app changes expected locationName-->
#                                                                 <div class="phs-locations-suggested" if.bind="allSuggestions.show.locations &amp;&amp; (allSuggestions.locations.city.length || allSuggestions.locations.state.length || allSuggestions.locations.country.length)" data-ph-at-id="suggested-locations" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-Kbmxpy">
#                                                                     <h3 data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-vbs30D">
#                                                                         <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1HL31LocationsText" data-ph-at-id="heading-text" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-ebcuVu">
#               Location
#             </ppc-content>
#                                                                     </h3>
#                                                                     <ul class="phs-locations-suggested-list" data-ph-at-id="suggested-data-list" data-ph-at-data-count="${allSuggestions.locations.length}" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-oZttro">
#                                                                         <li repeat.for="eachCity of allSuggestions.locations.city" class="phsLocationsSuggested_${$index}" data-ph-at-id="suggested-data-cities-list-item" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-AgvvSa">
#                                                                             <a ph-tevent="type_ahead_search" ref="linkEle" id="phs-lia_1_${$index}" href.bind="getUrl(linkEle, 'search-results', eachCity, 'qcity='+eachCity.city+'&amp;qstate='+eachCity.state+'&amp;qcountry='+eachCity.country)" data-ph-tevent-attr-trait59="location" data-ph-tevent-attr-trait60="${eachCity.name}" data-option-title="${eachCity.name}" data-category="${eachCity.name}" role="link" data-ph-at-id="suggested-data-link" data-ph-at-data-count="${eachCity.count}" data-ph-at-data-text="${eachCity.locationName_html}" data-ph-at-data-citystatecountry-text="${eachCity.cityStateCountry}" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-pyYulp">
#                                                                                 <span innerhtml="${(eachCity.locationName ? eachCity.locationName_html : eachCity.cityStateCountry) | sanitizeHTML}" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-OQQZaH"></span>
#                                                                                 <span if.bind="eachCity.isSuggested" class="suggested-location" data-ph-at-id="suggested-location" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-WHO8lL">
#                                                                                     <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1HL31CitySuggestedText" data-ph-at-id="suggested-location-text" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-QYUfQN">
#                  . suggested location
#                </ppc-content>
#                                                                                 </span>
#                                                                                 <span class="phs-jobs-count" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-c2fDZ4">${eachCity.count}</span>
#                                                                                 <span class="sr-only" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-TkzFVN">
#                                                                                     <span if.bind="eachCity.count == 1" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-IV2AvN">
#                                                                                         <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1HL31CitySuggestedJobText" data-ph-at-id="countLabel" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-RMw0LS">
#                  job
#                 </ppc-content>
#                                                                                     </span>
#                                                                                     <span if.bind="eachCity.count > 1" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-miFxKg">
#                                                                                         <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1HL31CitySuggestedJobsText" data-ph-at-id="countLabel" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-ccUXXl">
#                  jobs
#                 </ppc-content>
#                                                                                     </span>
#                                                                                 </span>
#                                                                             </a>
#                                                                         </li>
#                                                                         <li repeat.for="eachState of allSuggestions.locations.state" class="phsLocationsSuggested_${$index}" data-ph-at-id="suggested-data-states-list-item" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-EowCqj">
#                                                                             <a ph-tevent="type_ahead_search" ref="linkEle" id="phs-lia_2_${$index}" href.bind="getUrl(linkEle, 'search-results', eachState, 'qstate='+eachState.state+'&amp;qcountry='+eachState.country)" data-ph-tevent-attr-trait59="location" data-ph-tevent-attr-trait60="${eachState.name}" data-option-title="${eachState.name}" data-category="${eachState.name}" role="link" data-ph-at-id="suggested-data-link" data-ph-at-data-count="${eachState.count}" data-ph-at-data-text="${eachState.locationName_html}" data-ph-at-statecountry-text="${eachState.stateCountry}" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-dqAecS">
#                                                                                 <span innerhtml="${(eachState.locationName ? eachState.locationName_html : eachState.stateCountry) | sanitizeHTML}" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-p8KgOQ"></span>
#                                                                                 <span if.bind="eachState.isSuggested" class="suggested-location" data-ph-at-id="suggested-location" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-vAHBFF">
#                                                                                     <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1HL31StateSuggestedText" data-ph-at-id="suggested-location-text" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-7EHsAi">
#                  . suggested location
#                </ppc-content>
#                                                                                 </span>
#                                                                                 <span class="phs-jobs-count" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-zrhdkm">${eachState.count}</span>
#                                                                                 <span class="sr-only" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-2UPAnh">
#                                                                                     <span if.bind="eachState.count == 1" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-JESGBB">
#                                                                                         <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1HL31StateSuggestedJobText" data-ph-at-id="countLabel" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-gOUDej">
#                  job
#                 </ppc-content>
#                                                                                     </span>
#                                                                                     <span if.bind="eachState.count > 1" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-nvMnJX">
#                                                                                         <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1HL31StateSuggestedJobsText" data-ph-at-id="countLabel" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-MLqkZ0">
#                  jobs
#                 </ppc-content>
#                                                                                     </span>
#                                                                                 </span>
#                                                                             </a>
#                                                                         </li>
#                                                                         <li repeat.for="eachCountry of allSuggestions.locations.country " class="phsLocationsSuggested_${$index}" data-ph-at-id="suggested-data-countries-list-item" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-r1zOQx">
#                                                                             <a ph-tevent="type_ahead_search" ref="linkEle" id="phs-lia_3_${$index}" href.bind="getUrl(linkEle, 'search-results', eachCountry, 'qcountry='+eachCountry.name)" data-ph-tevent-attr-trait59="location" data-ph-tevent-attr-trait60="${eachCountry.name}" data-option-title="${eachCountry.name}" data-category="${eachCountry.name}" role="link" data-ph-at-id="suggested-data-link" data-ph-at-data-count="${eachCountry.count}" data-ph-at-data-text="${eachCountry.locationName_html}" data-ph-at-statecountry-text="${eachCountry.stateCountry}" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-dxlk9E">
#                                                                                 <span innerhtml="${(eachCountry.locationName ? eachCountry.locationName_html : eachCountry.stateCountry) | sanitizeHTML}" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-0LfNaL"></span>
#                                                                                 <span if.bind="eachCountry.isSuggested" class="suggested-location" data-ph-at-id="suggested-location" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-iQv7A3">
#                                                                                     <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1HL31CountrySuggestedText" data-ph-at-id="suggested-location-text" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-sBclIZ">
#                  . suggested location
#                </ppc-content>
#                                                                                 </span>
#                                                                                 <span class="phs-jobs-count" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-vBQOPK">${eachCountry.count}</span>
#                                                                                 <span class="sr-only" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-CItt0R">
#                                                                                     <span if.bind="eachCountry.count == 1" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-hYFwzw">
#                                                                                         <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1HL31CountrySuggestedJobText" data-ph-at-id="countLabel" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-QLATXh">
#                  job
#                 </ppc-content>
#                                                                                     </span>
#                                                                                     <span if.bind="eachCountry.count > 1" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-VPUVMG">
#                                                                                         <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1HL31CountrySuggestedJobsText" data-ph-at-id="countLabel" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-Dt42yH">
#                  jobs
#                 </ppc-content>
#                                                                                     </span>
#                                                                                 </span>
#                                                                             </a>
#                                                                         </li>
#                                                                     </ul>
#
#                                                                 </div>
#                                                                 <!--Jobs-->
#                                                                 <div class="phs-jobs-suggested" if.bind="allSuggestions.show.jobs" data-ph-at-id="suggested-jobs" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-NrI0uf">
#                                                                     <h3 data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-GhoLU4">
#                                                                         <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1HL32JobsText" data-ph-at-id="heading-text" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-lYzKPa">
#              Jobs
#             </ppc-content>
#                                                                     </h3>
#                                                                     <ul class="phs-jobs-list" data-ph-at-id="suggested-data-list" data-ph-at-data-count="${allSuggestions.jobs.length}" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-J5vPvT">
#                                                                         <li repeat.for="eachJob of allSuggestions.jobs" data-ph-at-id="suggested-data-list-item" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-Nm3JhP">
#                                                                             <a ph-tevent="type_ahead_search" id="phs-lia_0_${$index}" ref="linkEle" href.bind="getUrl(linkEle, 'job', eachJob)" data-ph-tevent-attr-trait59="jobId" data-ph-tevent-attr-trait60="${eachJob.jobSeqNo}" data-option-title="${eachJob.title}" data-title="${eachJob.title}" data-jobid="${eachJob.id}" role="link" data-ph-at-id="suggested-data-link" data-ph-at-job-title-text="${eachJob.title}" data-ph-at-job-id-text="${eachJob.jobId}" data-ph-at-job-seqno-text="${eachJob.jobSeqNo}" data-ph-at-job-location-text="${eachJob.location}" data-ph-at-job-category-text="${eachJob.category}" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-fI6sUD">
#                                                                                 <div class="phs-job-title" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-iej9Mq">
#                                                                                     <span class="sr-only" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-jaZUXV">
#                                                                                         <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1HL32JobTitleText" data-ph-at-id="jobtitle-text" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-Zy0nng">
#                  Job title
#                 </ppc-content>
#                                                                                     </span>
#                                                                                     <span innerhtml="${eachJob.title_html | sanitizeHTML}" data-ph-at-id="jobtitle-text" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-R2NYvJ"></span>
#                                                                                 </div>
#
#                                                                                 <div class="phs-job-info" if.bind="eachJob.location" data-ph-at-id="job-info" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-h2tO1x">
#                                                                                     <span class="phs-job-location" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-ndnOfM">
#                                                                                         <span class="sr-only" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-p2vVyF">
#                                                                                             <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1HL32JobLocationText" data-ph-at-id="joblocation-text" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-RHqH3s">
#                   Location
#                  </ppc-content>
#                                                                                         </span>
#                                                                                         ${eachJob.location}
#                                                                                     </span>
#                                                                                     <span class="phs-job-category" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-cuxgOJ">
#                                                                                         <span class="sr-only" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-rfSyPp">
#                                                                                             <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1HL32JobProfessionText" data-ph-at-id="jobcategory-text" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-D2hlxP">
#                   Profession
#                  </ppc-content>
#                                                                                         </span>
#                                                                                         ${eachJob.category}
#                                                                                     </span>
#                                                                                 </div>
#                                                                             </a>
#                                                                         </li>
#                                                                     </ul>
#                                                                 </div>
#                                                                 <!--Category-->
#                                                                 <div class="phs-categorys-suggested" if.bind="allSuggestions.show.categories" data-ph-at-id="suggested-categories" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-LDTrDG">
#
#                                                                     <h3 data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-kNc5Bt">
#                                                                         <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1HL33JobProfessionText" data-ph-at-id="heading-text" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-BJJrCU">
#              Profession
#             </ppc-content>
#                                                                     </h3>
#                                                                     <ul class="phs-categorys-suggested-list" data-ph-at-id="suggested-data-list" data-ph-at-data-count="${allSuggestions.categories.length}" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-QQXdcr">
#                                                                         <li repeat.for="eachCategory of allSuggestions.categories" data-ph-at-id="suggested-data-list-item" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-A6O8xR">
#                                                                             <a ph-tevent="type_ahead_search" id="phs-lia_0_${$index}" ref="linkEle" href.bind="getUrl(linkEle, 'category', eachCategory)" data-ph-tevent-attr-trait59="category" data-ph-tevent-attr-trait60="${eachCategory.category}" data-option-title="${eachCategory.category}" data-category="${eachCategory.category}" role="link" data-ph-at-id="suggested-data-link" data-ph-at-data-text="${eachCategory.key}" data-ph-at-data-count="${eachCategory.count}" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-bhb9PO">
#                                                                                 ${eachCategory.category}
#                                                                                 <span class="phs-jobs-count" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-Ca0KEP">${eachCategory.count}</span>
#                                                                                 <span class="sr-only" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-F01GSB">
#                                                                                     <span if.bind="eachCategory.count == 1" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-HorNg6">
#                                                                                         <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1HL33JobProfessionJobText" data-ph-at-id="countLabel" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-MhGUIp">
#                  job
#                 </ppc-content>
#                                                                                     </span>
#                                                                                     <span if.bind="eachCategory.count > 1" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-ghMe96">
#                                                                                         <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1HL33JobProfessionJobsText" data-ph-at-id="countLabel" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-VhASKm">
#                  jobs
#                 </ppc-content>
#                                                                                     </span>
#                                                                                 </span>
#                                                                             </a>
#                                                                         </li>
#                                                                     </ul>
#                                                                 </div>
#                                                                 <!--Recent Searches-->
#                                                                 <div class="phs-recentsearches-suggested" if.bind="allSuggestions.show.searched" data-ph-at-id="suggested-recentsearches" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-4aGfiI">
#                                                                     <h3 data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-WyH6Bf">
#                                                                         <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1HL34RecentserachText" data-ph-at-id="heading-text" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-fGh7zF">
#              Recent Searches
#             </ppc-content>
#                                                                     </h3>
#                                                                     <ul class="search-recentsearchs-list" data-ph-at-id="suggested-data-list" data-ph-at-data-count="${allSuggestions.searched.length}" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-pOQGXy">
#                                                                         <li repeat.for="eachKeyword of allSuggestions.searched" show.bind="$index < 3" data-ph-at-id="suggested-data-list-item" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-24FRpD">
#                                                                             <a ph-tevent="type_ahead_search" id="phs-lia_4_${$index}" ref="linkEle" data-ajax="false" data-option-title="${eachKeyword}" click.delegate="updateLocalStrWithRecentSearchDetails(eachKeyword)" href.bind="getUrl(linkEle, 'search-results', {keyword: eachKeyword}, 'keywords='+eachKeyword)" data-ph-tevent-attr-trait59="recent_keyword" data-ph-tevent-attr-trait60="${eachKeyword}" role="link" data-ph-at-id="suggested-data-link" data-ph-at-data-text="${eachKeyword}" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-updRnY">
#                                                                                 ${eachKeyword}
#                                                                             </a>
#                                                                         </li>
#                                                                     </ul>
#                                                                 </div>
#                                                                 <!--Suggested Keywords-->
#                                                                 <div class="phs-suggested-keywords-suggested" if.bind="allSuggestions.show.keywords &amp;&amp; !allSuggestions.show.jobs" data-ph-at-id="suggested-keywords" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-BiHp9M">
#                                                                     <h3 data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-HjbWWR">
#                                                                         <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1HL35SuggestedKeyText" data-ph-at-id="heading-text" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-ssjWdo">
#              Suggested keywords
#             </ppc-content>
#                                                                     </h3>
#                                                                     <ul class="phs-suggested-keywords-list" click.delegate="handleSelection($event)" data-ph-at-id="suggested-data-list" data-ph-at-data-count="${allSuggestions.keywords.length}" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-7rbg32">
#                                                                         <li repeat.for="eachKeyword of allSuggestions.keywords" show.bind="$index < 3" data-ph-at-id="suggested-data-list-item" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-CQWnou">
#                                                                             <a ph-tevent="type_ahead_search" id="phs-lia_5_${$index}" ref="linkEle" data-ajax="false" data-option-title="${eachKeyword}" click.delegate="updateLocalStrWithRecentSearchDetails(eachKeyword)" href.bind="inlineSearch ? 'javascript:void(0)' : getUrl(linkEle, 'search-results', {keyword: eachKeyword}, 'keywords='+eachKeyword)" data-ph-tevent-attr-trait59="recent_keyword" data-ph-tevent-attr-trait60="${eachKeyword}" role="link" data-ph-at-id="suggested-data-link" data-ph-at-data-text="${eachKeyword}" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-HITvsJ">
#                                                                                 ${eachKeyword}
#                                                                             </a>
#                                                                         </li>
#                                                                     </ul>
#                                                                 </div>
#                                                             </div>
#                                                             <button class="close-suggestions-btn" data-ph-at-id="clear-globalsearch-link" click.delegate="showDropDown = false" aria-label="Close search suggestion" key-aria-label="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1OffScreenCloseBtnAriaLabelText" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-VVdvML">
#                                                                 <i class="icon icon-cancel" aria-hidden="true" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-eFApuC"></i>
#                                                                 <span class="sr-only" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-0zIsh5">
#                                                                     <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1OffScreenCloseBtnText" data-ph-at-id="clear-globalsearch-text" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-Js2UzV">
#             Close search suggestion
#            </ppc-content>
#                                                                 </span>
#                                                             </button>
#                                                         </div>
#                                                     </input></div>
#                                                 </div>
#                                                 <div class="col-xs-2" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-utlBcv">
#                                                     <span class="input-group-btn" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-KYdeFT">
#                                                         <button type="button" role="button" data-ph-at-id="globalsearch-button" click.delegate="handleSubmitClick({'checkValidation': false})" class="btn primary-button btn-lg phs-search-submit" aria-label="Find jobs" key-aria-label="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1FindjobsBtnAriaLabelText" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-7HDrYh">
#                                                             <ppc-content type="icon" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-IRMaNH">
#                                                                 <i class="icon icon-search" aria-hidden="true" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-Cse1mR"></i>
#                                                             </ppc-content>
#                                                             <span data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-rUJPN7">
#                                                                 <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1FindjobsBtnText" data-ph-at-id="globalsearch-button-text" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-V5Dmhc">
#           Find jobs
#          </ppc-content>
#                                                             </span>
#                                                         </button>
#                                                     </span>
#                                                 </div>
#                                             </div>
#                                         </div>
#                                     </form>
#                                     <div class="sr-only" aria-live="assertive" aria-atomic="true" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-zXMDoo">
#                                         <span if.bind="!searchValue.length &amp;&amp; gsClrTxt" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-9W8Dvm">
#                                             <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1OffScreenClearedText" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-9Vbxes">
#       Text cleared
#      </ppc-content>
#                                         </span>
#                                     </div>
#                                     <div class="sr-only" aria-live="assertive" aria-atomic="true" if.bind="commonService.getLocale() != 'fr_ca'" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-bI2dHK">
#                                         <span if.bind="showDropDown &amp;&amp; showJobSuggestions &amp;&amp; searchValue.length >= 3 &amp;&amp; allSuggestions.locations.city.length + allSuggestions.locations.state.length + allSuggestions.locations.country.length + allSuggestions.jobs.length + allSuggestions.categories.length + allSuggestions.searched.length + allSuggestions.keywords.length > 0" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-oZ99E7">${allSuggestions.locations.city.length + allSuggestions.locations.state.length + allSuggestions.locations.country.length + allSuggestions.jobs.length + allSuggestions.categories.length + allSuggestions.searched.length + allSuggestions.keywords.length} <ppc-cpntent key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1OffScreenResultLengthText" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-epuheA">suggestions are available Use tab or up and down arrows keys to access.</ppc-cpntent>
#                                         </span>
#                                         <span if.bind="searchValue.length >= 3 &amp;&amp; allSuggestions.locations.city.length + allSuggestions.locations.state.length + allSuggestions.locations.country.length + allSuggestions.jobs.length + allSuggestions.categories.length + allSuggestions.searched.length + allSuggestions.keywords.length == 0" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-jOg2SA">
#                                             <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGSHeading1OffScreenNoSuggestionsNeText" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-E6mY5y">No suggestions available</ppc-content>
#                                         </span>
#                                     </div>
#                                     <!-- <div class="sr-only" aria-live="assertive" aria-atomic="true">
#                                         <span if.bind="!showDropDown && !searchValue.length"><ppc-content key="homeGlobalsearchHeading1OffScreenCollapsedText">Collapsed</ppc-content></span>
#                                     </div> -->
#                                     <!-- Live region start -->
#                                     <!-- <span aria-live="assertive" aria-atomic="true" class="sr-only">
#                                         <span if.bind="showDropDown && showAllJobCategories && !searchValue.length">
#                                             <ppc-content key="homeGlobalsearchHeading1OffScreenSelectProfessionText">Use tab or up and down arrows keys to access profession. Expanded</ppc-content>
#                                         </span>
#                                     </span> -->
#                                     <!-- Live region end -->
#
#                                     <!-- Keyword search information -->
#                                     <div class="learn-keyword-search-block" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-dX81c3"><button onclick="keyword$SearchInfo$(this,true)" aria-label="click on this to view more info" class="learn-more-info-btn" tool-tip="Learn more about search  jobs" key-tool-tip="p3mrzw-ph-global-search-v3-default-globalSearchLearnMoreKeywordsSearchBtToolTipText" key-aria-label="p3mrzw-ph-global-search-v3-default-globalSearchLearnMoreKeywordsSearchBtnAriaLabelTextText" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-oSGw2v"><i class="icon icon-info-o" aria-hidden="true" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-6aq0zR"></i><span data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-0HG88K"><ppc-content key="p3mrzw-ph-global-search-v3-default-globalSearchLearnMoreKeywordsSearchBtnText" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-451LuE">Learn more</ppc-content></span></button>
#                                         <div class="learn-more-info hide" role="alert" aria-atomic="false" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-tB8KE6">
#                                             <span id="lear_more_info" class="hide" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-9wdQwx"><span class="learn-info-ext" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-RSjino"><ppc-content key="p3mrzw-ph-global-search-v3-default-globalSearchLearnMoreKeywordsSearchDescInfoExtText" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-zm6D7Z">Start a new search with a keyword or using the filters below. Ideas for your keyword search: job ID, any skill or title, for example C++, AI, or “Program Manager.”</ppc-content></span>
#                                             <span class="learn-info-ext-1" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-IXe2qJ"><ppc-content key="p3mrzw-ph-global-search-v3-default-globalSearchLearnMoreKeywordsSearchDescInfoExtText1" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-OQO5gG">Using double quotations (“”) searches for an exact phrase match.</ppc-content></span>
#                                             </span>
#                                             <span id="lear_more_info_int" class="hide" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-CifyqR"><span class="learn-info-int" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-7tsh2q"><ppc-content key="p3mrzw-ph-global-search-v3-default-globalSearchLearnMoreKeywordsSearchDescInfoIntText" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-j8NbEa">Start a new search with a keyword or using the filters below. Ideas for your keyword search: hiring manager alias, job ID, any skill or title, for example C++, AI, or “Program Manager.”</ppc-content></span>
#                                             <span class="learn-info-int-1" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-98Y2Ac"><ppc-content key="p3mrzw-ph-global-search-v3-default-globalSearchLearnMoreKeywordsSearchDescInfoIntText1" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-QLgNdt">Using double quotations (“”) searches for an exact phrase match.</ppc-content></span></span>
#                                             <button onclick="keyword$SearchInfo$(this,false)" onkeydown="closeLmpopUp(this,event)" class="close-keyword-info" aria-label="close learn more popup" key-aria-label="p3mrzw-ph-global-search-v3-default-globalSearchLearnMoreKeywordsSearchCloseAriaLabelText" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-twde9Z"><i class="icon icon-cancel" aria-hidden="true" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-SoLVSr"></i></button>
#                                         </div>
#                                     </div>
#                                 </script><script type="text/x-ph-tmpl" id="ph-facets-v1-view-external-1566561389257">
#                                 <div class="phs-refine-block" role="region" aria-labelledby="facet-search-block" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-bog50P">
#                                     <a href="#content" class="skip-block" aria-label="Skip to Show Results" key-aria-label="lqzfz5-ph-facets-v1-view-external-searchFacetsSkipBlockLinkAriaLabelText" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-k6nx4P"><ppc-content key="lqzfz5-ph-facets-v1-view-external-searchFacetsSkipBlockLinkText" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-ckAcok">Skip to Show Results</ppc-content></a>
#                                     <div class="phs-hide-filter" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-mxfH7Y">
#                                         <a href="javascript:void(0)" click.delegate="hideFacetFilter()" aria-label="Close the filter" key-aria-label="lqzfz5-ph-facets-v1-view-external-searchFacetsLinkAriaLabel" tabindex="0" role="button" data-ph-at-id="mobile-facet-filter-close-link" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-5YU1od">
#                                             <ppc-content type="icon" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-1niQag">
#                                                 <i class="icon icon-cancel" aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-5CQZ1r"></i>
#                                             </ppc-content>
#                                         </a>
#                                     </div>
#                                     <div class="panel panel-default main-panel" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-xVf303">
#                                         <div class="panel-heading" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-LyUf7J">
#                                             <h2 class="panel-title" id="facet-search-block" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-Sxc1TP">
#                                                 <ppc-content key="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1Text" data-ph-at-id="heading-text" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-mzDgaF">
#          Refine your search
#        </ppc-content>
#                                             </h2>
#                                         </div>
#                                         <div class="panel-heading mobile-toggle-button" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-m379cG">
#                                             <h2 class="panel-title" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-qhbIhx">
#                                                 <button click.delegate="facetKey.refineOpen = !facetKey.refineOpen" aria-expanded="${facetKey.refineOpen ? 'false' : 'true'}" aria-label="toggle refine search" key-aria-label="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1BtnAriaLabelText" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-qEcpqE">
#                                                     <ppc-content key="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1BtnText" data-ph-at-id="mobile-heading-text" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-ICqwMf">
#           Refine your search
#         </ppc-content>
#                                                     <ppc-content type="icon" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-7TXvJM">
#                                                         <i class="${facetKey.refineOpen ? 'icon icon-up-arrow' : 'icon icon-down-arrow'}" aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-I87dV0"></i>
#                                                     </ppc-content>
#                                                 </button>
#                                             </h2>
#                                         </div>
#                                     </div>
#                                     <div class="phs-filter-panels ${facetKey.refineOpen ? 'hide' : 'show'}" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-0BBTbM">
#                                         <div class="panel panel-default refine-widget" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-K7McKK">
#                                             <!-- <div class="panel-heading">
#                                                 <span class="panel-title">
#                                                     <button class="facet-menu" click.trigger="facetKey.toggleOpen = !facetKey.toggleOpen" keyup.trigger="($event.keyCode === 27)? (facetKey.toggleOpen = false):''" aria-expanded="${facetKey.toggleOpen ? 'true' : 'false'}" aria-label="Keywords Search" key-aria-label="searchFacetsHeadingLevel1KeywordsSearchBtnAriaLabelText">
#                                                         <ppc-content key="searchFacetsHeadingLevel1KeywordsSearchBtnText" data-ph-at-id="facet-accordian-text">Keywords</ppc-content>
#                                                         <ppc-content type="icon">
#                                                             <i class="${facetKey.toggleOpen ? 'icon icon-up-arrow' : 'icon icon-down-arrow'}" aria-hidden="true"></i>
#                                                         </ppc-content>
#                                                     </button>
#                                                 </span>
#                                             </div> -->
#                                             <div class="panel-collapse collapse in" data-ph-at-id="facet-sub-search" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-UhSosE">
#                                                 <div class="search-container" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-9fwok9">
#                                                     <form data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-XgLI3G">
#                                                         <div class="input-group input-group-sm has-feedback-search" role="search" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-GbyLQK">
#                                                             <!-- <label class="sr-only" aria-hidden="true">
#                                                                 <ppc-content key="searchFacetsHeadingLevel1SearchWithinkeywordsText" data-ph-at-id="sub-search-textbox-text">
#                                                                     Search keywords within results
#                                                                 </ppc-content>
#                                                             </label> -->
#                                                             <input focus.trigger="clrTxt = 0" type="text" value.bind="searchParams.subsearch" placeholder="Search within results" key-placeholder="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1SearchWithinkeywordsPlaceHolderText" autocomplete="off" class="form-control" id="sub_search_textbox" maxlength="200" data-ph-at-id="sub-search-textbox" aria-label="Search within results" key-aria-label="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1SearchWithinkeywordsAriaLabelText" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-Trs4c3">
#                                                             <span class="sr-tooltip" aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-c87Tg2"><ppc-content key="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1SearchWithinkeywordstoolTipText" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-p6PNSg">Search within results</ppc-content></span>
#                                                             <button keyup.trigger="clrTxt = 1" mouseup.trigger="clrTxt = 1" class="clear-textbox" id="clear-sub-search-textbox" click.delegate="clearSubSearchAndCallSearch()" onclick="setTimeout(function(){document.getElementById('sub_search_textbox').focus();},1000)" if.bind="(searchParams.subsearch.trim()).length > 0" role="button" key-role="2ok9Ve-lqzfz5-ph-facets-v1-view-external-btnRole" aria-label="Clear text" key-aria-label="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1SKWRClearTextBtnAriaLabelText" tip-toolinfo="Clear text" key-tip-toolinfo="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1SKWRCClearTextBtnTooltipText" type="button" data-ph-at-id="sub-search-textbox-clear-link" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-ywzd6y">
#                                                                 <ppc-content type="icon" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-vKlKIF">
#                                                                     <i class="icon icon-cancel" aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-OmVbsf"></i>
#                                                                 </ppc-content>
#                                                                 <span class="sr-only" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-o2JBMF">
#                                                                     <ppc-content key="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1SKWRClearTextOffScreenText" data-ph-at-id="sub-search-textbox-clear-text" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-eWWcX6">
#               Clear text
#              </ppc-content>
#                                                                 </span>
#                                                             </button>
#                                                             <span class="input-group-btn" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-yklRE6">
#                                                                 <button type="submit" class="btn btn-default ${(searchParams.subsearch.trim()).length > 0 ? '': 'disabled'}" click.delegate="filterSearch()" aria-label="Search" key-aria-label="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1SKWRCSearchSubmitBtnAriaLabelText" role="button" key-role="DNVvxt-lqzfz5-ph-facets-v1-view-external-btnRole" tip-toolinfo="Search jobs" key-tip-toolinfo="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1SKWRCSubmitBtnTooltipText" data-ph-at-id="sub-search-textbox-button" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-oe99im">
#                                                                     <i class="icon icon-search" aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-h2QsHV"></i>
#                                                                 </button>
#                                                             </span>
#                                                         </input></div>
#                                                     </form>
#                                                     <div class="sr-only" role="alert" aria-relevant="additions text" aria-label="Text cleared" if.bind="!searchParams.subsearch.length &amp;&amp; clrTxt" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-asgkE0">
#                                                         <ppc-content key="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1SKWRCClearTextOffScreenText" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-XVs8Eq">
#           Text cleared
#          </ppc-content>
#                                                     </div>
#                                                     <!-- <div class="learn-keyword-search-block"><button onclick="keyword$SearchInfo$(this,true)" aria-label="Learn more" class="learn-more-info-btn" key-aria-label="searchFacetsHeadingLevel1LearnMoreKeywordsSearchBtnAriaLabelTextText"><i class="icon icon-info-o" aria-hidden="true"></i><span><ppc-content key="searchFacetsHeadingLevel1LearnMoreKeywordsSearchBtnText">Learn more</ppc-content></span></button>
#                                                         <div class="learn-more-info hide" role="alert">
#                                                             <span id="lear_more_info" if.bind="commonService.getSiteType() != 'internal'"><ppc-content key="searchFacetsHeadingLevel1LearnMoreKeywordsSearchDescInfoText">You can enter multiple keywords with a comma(,) or add separately. You can use keywords and also search by job ID, "remote".</ppc-content></span>
#                                                             <span id="lear_more_info_int" if.bind="commonService.getSiteType() == 'internal'"><ppc-content key="searchFacetsHeadingLevel1LearnMoreKeywordsSearchDescInfoText">You can enter multiple keywords with a comma(,) or add separately. You can use keywords and also search by job ID, "remote", or hiring manager alias.</ppc-content></span>
#                                                             <button onclick="keyword$SearchInfo$(this,false)" class="close-keyword-info" aria-label="close keyword search popup" key-aria-label="searchFacetsHeadingLevel1LearnMoreKeywordsSearchCloseAriaLabelText"><i class="icon icon-cancel" aria-hidden="true"></i></button>
#                                                         </div>
#                                                     </div> -->
#                                                 </div>
#                                             </div>
#
#                                         </div>
#                                         <div class="panel panel-default refine-widget" repeat.for="facetKey of searchFacetKeys" landing-facet-hide="${facetDisplayNames[facetKey.key]}" data-ph-at-id="facet-${facetKey.key}" data-ph-at-text="${facetKey.key}" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-a1seui">
#                                             <!-- facet heading { bindings :  facetKey }-->
#                                             <div class="panel-heading" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-hoHIq8">
#                                                 <span class="panel-title" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-deX2cm">
#                                                     <button class="facet-menu" aria-label="${facetDisplayNames[facetKey.key]}" aria-expanded="${facetKey.visible ? 'true' : 'false'}" keyup.trigger="($event.keyCode === 27)? (facetKey.visible = false):''" click.delegate="adjustAccordian($index)" data-ph-at-id="facet-heading-link" data-ph-at-text="${facetDisplayNames[facetKey.key]}" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-uHxChv">
#                                                         ${facetDisplayNames[facetKey.key]}
#                                                         <ppc-content type="icon" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-1z3rWp">
#                                                             <i class="${facetKey.visible ? 'icon icon-up-arrow' : 'icon icon-down-arrow'}" aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-UcYCva"></i>
#                                                         </ppc-content>
#                                                     </button>
#                                                 </span>
#                                             </div>
#                                             <!-- facet options block -->
#                                             <div class="panel-collapse collapse in" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-nvUI3r">
#                                                 <div class="panel-body" if.bind="facetKey.visible" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-B1fXQw">
#                                                     <!-- search field and button -->
#                                                     <div class="phs-facet-innersearch" if.bind="facetRef.filtered.length >= 4 || facetClrTxt == 0 || focusClrTxtBtn" data-ph-at-id="facet-innersearch" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-dcD64k">
#                                                         <!-- <label for="inner_${filterKey}" class="sr-only"><span><ppc-content key="searchText">Search</ppc-content></span>${facetKey.key</label> -->
#                                                         <input type="search" id="facetInput-${$index}" focus.trigger="facetClrTxt = 0" class="form-control search-box" value.bind="filterKey &amp; debounce:100" placeholder="${facetPlaceholderNames[facetKey.key]}" data-ph-at-id="facet-textbox" aria-label="${facetPlaceholderNames[facetKey.key]}" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-1UBhO4">
#                                                         <button keyup.trigger="facetClrTxt = 1" mouseup.trigger="facetClrTxt = 1" focus.trigger="focusClrTxtBtn = 1" blur.tirgger="focusClrTxtBtn = 0" class="clear-textbox" id="clear-sub-search-textbox" click.delegate="filterKey = ''" onclick="setTimeout(function(){document.getElementById('facetInput').focus();},1000)" if.bind="filterKey.length > 0" role="button" key-role="a6Mtgd-lqzfz5-ph-facets-v1-view-external-btnRole" aria-label="Clear text" key-aria-label="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1ClearBtnAriaLabelText" tip-toolinfo="Clear text" data-ph-at-id="facet-clear-textbox-link" key-tip-toolinfo="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1ClearBtnToolTipText" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-atQe9E">
#                                                             <ppc-content type="icon" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-zuULpp">
#                                                                 <i class="icon icon-cancel" aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-AUCXBi"></i>
#                                                             </ppc-content>
#                                                             <span class="sr-only" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-MpFHrW">
#                                                                 <ppc-content key="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1ClearBtnText" data-ph-at-id="facet-clear-textbox-link-text" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-RPch07">
#              Clear text
#             </ppc-content>
#                                                             </span>
#                                                         </button>
#                                                         <button class="innersearch-trigger" aria-label="Search in ${facetKey.key}" role="button" key-role="eN6sc7-lqzfz5-ph-facets-v1-view-external-btnRole" tip-toolinfo="Search jobs" key-tip-toolinfo="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1ClearBtnsearchToolTipText" data-ph-at-id="facet-inputbox-search-link" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-dOe1C7">
#                                                             <ppc-content type="icon" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-MFbR4A">
#                                                                 <i class="icon icon-search" aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-0DiSU0"></i>
#                                                             </ppc-content>
#                                                         </button>
#                                                     </input></div>
#                                                     <div class="sr-only" aria-relevant="additions text" aria-label="Text cleared" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-QSmuSF">
#                                                         <span if.bind="!filterKey.length &amp;&amp; facetClrTxt" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-lOFGl8"><ppc-content key="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1ClearTextOffScreenText" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-RH3pEE">
#           Text cleared
#          </ppc-content></span>
#                                                     </div>
#                                                     <!-- facet options -->
#
#                                                     <div class="phs-facet-results" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-gOyG16">
#                                                         <div ref="facetRef" filtered.bind="searchFacets[facetKey.key] | searchFilter:filterKey:'name'" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-T34Hj9">
#                                                             <div class="no-facet-results" aria-live="assertive" aria-atomic="true" data-ph-at-id="no-facet-results" data-ph-at-search-keyword-text="${filterKey}" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-LbGIwh">
#                                                                 <span if.bind="facetRef.filtered.length === 0 &amp;&amp; filterKey.length >= 3" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-mLY4NH">
#                                                                     <span data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-oUujRm"><ppc-content key="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1NoresultDatafcetText" data-ph-at-id="nodata-text" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-J106JZ">
#               No results found for
#              </ppc-content></span> "${filterKey}"
#                                                                 </span>
#
#                                                                 <span if.bind="facetRef.filtered.length > 0 &amp;&amp; filterKey.length >= 3 &amp;&amp; !facetClrTxt" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-WlS18S">
#                                                                     <span data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-UnndCr"><ppc-content key="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1ShowResultText1" data-ph-at-id="showing-text" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-HeYlFl">
#               Showing
#              </ppc-content></span> ${facetRef.filtered.length} <span data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-aQUE8z"><ppc-content key="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1ShowResultText2" data-ph-at-id="results-for-text" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-NI9XLo">
#               results for
#              </ppc-content></span> "${filterKey}"
#                                                                 </span>
#                                                             </div>
#                                                         </div>
#                                                         <ul data-ph-at-id="facet-results-list" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-ro2kL7">
#                                                             <li repeat.for="facet of facetRef.filtered" data-ph-at-id="facet-results-item" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-eVJPfi">
#                                                                 <label class="phs-checkbox input-check-group" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-I6UzSJ">
#                                                                     <input type="checkbox" model.bind="facet" checked.bind="facet.checked" change.delegate="filterChanged(facet, facetKey.key)" role="checkbox" key-role="lqzfz5-ph-facets-v1-view-external-chkboxRole" data-ph-at-id="facet-checkbox" aria-label="${facet.name} ${facet.count} ${(facet.count == 1 ? 'job' : 'jobs')}" key-aria-label="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1ChekBoxAriaLabel" data-ph-at-text="${facet.name}" data-ph-at-count="${facet.count}" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-45xeTf">
#                                                                     <span class="checkbox" aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-qusfTm">
#                                                                     </span>
#                                                                     <span class="result-text" aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-SaVTMp">${facet.name}
#                                                                         <span class="result-jobs-count" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-nGOOQq">
#                                                                             <span class="symbol" aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-mDgfey">(</span>${facet.count}<span class="sym" aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-Sl3WlA">)</span></span><span class="sr-only" if.bind="facet.count == 1" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-Aqo6CD"><ppc-content data-ph-at-id="countLabel" key="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1JobSingularlText" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-E0cnIa">
#                job
#               </ppc-content></span><span class="sr-only" if.bind="facet.count > 1" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-TNNA6J"><ppc-content data-ph-at-id="countLabel" key="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1JobsPluralText" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-wEGd0L">
#                jobs
#               </ppc-content></span>
#                                                                     </span>
#                                                                 </input></label>
#                                                             </li>
#                                                         </ul>
#                                                     </div>
#                                                 </div>
#                                             </div>
#                                         </div>
#                                     </div>
#                                     <!-- <div class="phs-bottom-hide-filter">
#                                         <a href="javascript:void(0)" click.delegate="handleDoneButtonClick()" class="btn primary-button btn-block" aria-label="Refine Search" key-aria-label="refineSearchBtnLabel" role="button" key-role="btnRole" data-ph-at-id="mobile-facet-filter-done-button">
#                                             <ppc-content key="refineSearch" data-ph-at-id="mobile-facet-filter-done-button">
#                                                 Refine Search
#                                             </ppc-content>
#                                         </a>
#                                     </div> -->
#                                 </div>
#                                 <!-- static text for internal -->
#                                 <!-- <div class="hiring-content-block" if.bind="commonService.getSiteType() == 'internal'">
#                                     <div class="hiring-main-block">
#                                         <h2>
#                                             <ppc-content key="searchFacetsHeadingLevel2InternalJobsSearchText">Internal job search</ppc-content>
#                                         </h2>
#                                         <p>
#                                             <ppc-content key="searchFacetsHeadingLevel2InternalJobsSearchDescText">Looking for a job posted under a specific hiring manager? Enter their alias in the search bar at the top or in the keyword search and any jobs listing them as the hiring manager will be displayed. </ppc-content>
#                                         </p>
#                                     </div>
#                                 </div> -->
#                             </script><link rel="stylesheet" type="text/css" href="https://prodcmscdn.azureedge.net/careerconnectresources/p/MICRUS/tenantcss/main-1568887295309.css" id="tenantcss"><script snippet_id="GTM-HEAD-143">(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&amp;l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-MP6J282');</script><script async="" src="https://web.vortex.data.microsoft.com/collect/v1/t.js?ver='2.1'&amp;name='Ms.Webi.PageView'&amp;time='2019-09-28T11%3A24%3A24.136Z'&amp;os='MacOS'&amp;appId='JS%3ACareersbeta'&amp;-ver='1.0'&amp;-impressionGuid='e3de4559-3a3d-46c3-8ccd-ce855de39edc'&amp;-pageName='Search%20results%20%7C%20Find%20available%20job%20openings%20at%20Microsoft'&amp;-uri='https%3A%2F%2Fcareers.microsoft.com%2Fus%2Fen%2Fsearch-results%3Fkeywords%3Dphp'&amp;-market='en_us'&amp;-pageType='search-results'&amp;-resHeight=900&amp;-resWidth=1440&amp;-pageTags='%7B%22metaTags%22%3A%7B%7D%7D'&amp;-behavior=0&amp;*baseType='Ms.Content.PageView'&amp;*cookieEnabled=true&amp;*isJs=true&amp;*title='Search%20results%20%7C%20Find%20available%20job%20openings%20at%20Microsoft'&amp;*isLoggedIn=true&amp;*flashInstalled=false&amp;ext-app-env='prod'&amp;ext-javascript-ver='1.1'&amp;ext-javascript-libVer='4.2.14'&amp;ext-javascript-domain='careers.microsoft.com'&amp;ext-javascript-userConsent=false&amp;ext-user-localId='t%3A306118835119657A30371567551963BC'&amp;$mscomCookies=false"></script><script type="text/javascript" src="https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE1xHWh"></script><style type="text/css">.aurelia-hide { display:none !important; }</style><script type="text/javascript" src="https://prodcmscdn.azureedge.net/ctr-impressions/ctr_controller.min.js"></script><script type="text/javascript" src="https://prodcmscdn.azureedge.net/ctr-impressions/ctr_file.min.js"></script></head>
#  <body class="search-results-page" data-ph-id="ph-page-element-page19-E5btOp" aurelia-app="main"><noscript snippet_id="GTM-BODY-143">&lt;iframe src="\&amp;quot;https://www.googletagmanager.com/ns.html?id=GTM-MP6J282\&amp;quot;height=\&amp;quot;0\&amp;quot;" width="\&amp;quot;0\&amp;quot;" style="\&amp;quot;display:none;visibility:hidden\&amp;quot;"&gt;&lt;/iframe&gt;</noscript>
#   <div class="ph-header" data-ph-id="ph-page-element-page19-2uzHAm"><section class="ph-widget ph-widget-layout ppc-section ph-widget-target" view="short-header" type="static" instance-id="jt9mae" data-ph-id="short-header-CPGm9Q" original-view="short-header" as-element="short-header" data-widget="short-header"><div as-element="short-header" data-widget="short-header" view="short-header" original-view="short-header" type="static" instance-id="jt9mae" theme="default" class="ph-widget-target short-header-default" data-ph-id="ph-page-element-short-header-jt9mae-KpxXiQ">
#  <div class="hero-block short-header ph-widget-box" data-ph-id="ph-page-element-short-header-jt9mae-9m6yqF">
#   <!-- Header -->
#   <header data-ph-id="ph-page-element-short-header-jt9mae-5HJ1QF">
#    <!--top-header start-->
#    <div class="beta-container" data-ph-id="ph-page-element-short-header-jt9mae-8KULKF">
#     <!-- <div id="betaNotifier" class="beta-notifier hide" role="region" aria-label="Welcome to the Beta Version of our new Microsoft Careers Site">
#                     <div class="container">
#                         <div class="beta-paragraph">
#                             <span class="p-group">
#                                 <p><ppc-content key="betaVersionTxtNew1">Welcome to the Beta Version of our new Microsoft Careers Site! Please</ppc-content><a href="https://aka.ms/externalcareersfeedback" target="_blank" key-target="careers" ph-tevent="goto_click" data-ph-tevent-attr-trait256="Microsoft feedback form" role="link"><ppc-content key="giveUsFeedbackText"> give us feedback</ppc-content></a> as you search and apply. You can see additional jobs at our<a href="https://careers.microsoft.com/" target="_blank" key-target="careers" ph-tevent="goto_click" data-ph-tevent-attr-trait256="main site" role="link"><ppc-content key="careersSiteLinkTextNew1"> main site.</ppc-content></a><ppc-content key="etaVersionTxt2New1"> For accessibility support, please contact</ppc-content><a href="mailto:askgta@microsoft.com" ph-tevent="goto_click" data-ph-tevent-attr-trait256="Microsoft Disability Recruiting Team." role="link"><ppc-content key="microsoftDisabilityRecruitingTeamLinkTextNew1"> Microsoft Disability Recruiting Team.</ppc-content></a></p>
#                             </span>
#                             <button class="close-btn" onclick="ph$Msft$Custom.set_Cookie_For_FeedBack()" aria-label="Close banner" key-aria-label="closeBannerText" ph-tevent="header_notification_close_click">
#                                 <i class="icon icon-cancel" aria-hidden="true"></i>
#                             </button>
#                         </div>
#                     </div>
#                 </div> -->
#     <div id="multy-lang-betanotifier" class="multy-lang-bn show" role="region" aria-label="Important message from Microsoft" data-ph-id="ph-page-element-short-header-jt9mae-KV0aBq">
#      <div class="container" data-ph-id="ph-page-element-short-header-jt9mae-KlW7cn">
#       <div class="beta-paragraph ref-class" data-ph-id="ph-page-element-short-header-jt9mae-uWlmry">
#        <div class="p-group" id="multy-para-list" aria-live="assertive" aria-atomic="true" data-ph-id="ph-page-element-short-header-jt9mae-Tuxvfn">
#         <p id="multy-lang-def" lang="en" data-ph-id="ph-page-element-short-header-jt9mae-UC5Nr2"><span data-ph-id="ph-page-element-short-header-jt9mae-Qztmlh">
#           <ppc-content key="short-header-careersDefaultCookiesInfoText" data-ph-id="ph-page-element-short-header-jt9mae-7AvHoC">This site uses cookies for analytics, personalized content and ads. By continuing to browse this site, you agree to this use.</ppc-content></span><a key-ph-href="short-header-careersDefaultCookiesLinkurl" aria-label="Learn more about cookies and Microsoft Privacy policy opens in a new tab" id="default-link" key-aria-label="short-header-careersDefaultCookiesLabelText" key-target="short-header-careersDefaultCookiesTargetValue" target="_blank" ph-tevent="goto_click" data-ph-tevent-attr-trait256="learn more" role="link" data-ph-id="ph-page-element-short-header-jt9mae-AygbuJ" class="au-target" au-target-id="9" href="https://careers.microsoft.com/us/en/privacyandcookies" data-ph-href="privacyandcookies">
#           <ppc-content key="short-header-careersDefaultCookiesLinkText" data-ph-id="ph-page-element-short-header-jt9mae-j5Hf2B">Learn more</ppc-content></a>
#          <ppc-content key="short-header-careersDefaultCookiesInfoText1" data-ph-id="ph-page-element-short-header-jt9mae-M3dQTg">.</ppc-content></p>
#        </div>
#        <div class="select-list" data-ph-id="ph-page-element-short-header-jt9mae-l3GXHB">
#         <select id="multy-lang-combo" aria-label="select cookie language" key-aria-label="short-header-careersSelectCookieAriaLabelText" data-ph-id="ph-page-element-short-header-jt9mae-TQ5wxw"><option value="" slected="">Language</option><option value="AustriaGER">Austria-GER</option><option value="BelgiumDUT">Belgium-DUT</option><option value="BelgiumFRE">Belgium-FRE</option><option value="BulgariaBUL">Bulgaria-BUL</option><option value="CroatiaCRO">Croatia-CRO</option><option value="CyprusENG">Cyprus-ENG</option><option value="CyprusGRE">Cyprus-GRE</option><option value="Czech" republiccz="">Czech Republic-CZ</option><option value="DenmarkDAN">Denmark-DAN</option><option value="EstoniaEST">Estonia-EST</option><option value="FinlandFIN">Finland-FIN</option><option value="FranceFRE">France-FRE</option><option value="GermanyGER">Germany-GER</option><option value="GreeceGRE">Greece-GRE</option><option value="HungaryHUN">Hungary-HUN</option><option value="IcelandICE">Iceland-ICE</option><option value="IrelandENG">Ireland-ENG</option><option value="IrelandGAE">Ireland-GAE</option><option value="ItalyIT">Italy-IT</option><option value="LatviaLV">Latvia-LV</option><option value="LiechtensteinGER">Liechtenstein-GER</option><option value="LithuaniaLT">Lithuania-LT</option><option value="LuxembourgFRE">Luxembourg-FRE</option><option value="LuxembourgGER">Luxembourg-GER</option><option value="MaltaMT">Malta-MT</option><option value="NetherlandsNL">Netherlands-NL</option><option value="NorwayNB">Norway-NB</option><option value="PolandPL">Poland-PL</option><option value="PortugalPT">Portugal-PT</option><option value="RomaniaRO">Romania-RO</option><option value="SlovakiaSK">Slovakia-SK</option><option value="SloveniaSL">Slovenia-SL</option><option value="SpainES">Spain-ES</option><option value="SwedenSE">Sweden-SE</option><option value="SwitzerlandFRE">Switzerland-FRE</option><option value="SwitzerlandGER">Switzerland-GER</option><option value="SwitzerlandIT">Switzerland-IT</option><option value="United" kingdomeng="">United Kingdom-ENG</option></select>
#         <i class="icon icon-down-arrow" aria-hidden="true" data-ph-id="ph-page-element-short-header-jt9mae-xVm9Wh"></i>
#        </div>
#       </div>
#       <div class="new-p-group" data-ph-id="ph-page-element-short-header-jt9mae-IoH4mK">
#        <div id="multy-para-list-country" aria-live="assertive" aria-atomic="true" data-ph-id="ph-page-element-short-header-jt9mae-jFw9JR">
#        </div>
#        <button class="lang-close-btn au-target" onclick="ph$Msft$Custom.set_Multy_Lang_Cookie()" aria-label="Close message" key-aria-label="short-header-careersCloseMsgText" ph-tevent="header_notification_close_click" data-ph-id="ph-page-element-short-header-jt9mae-gbHVo4" au-target-id="10"> <i class="icon icon-cancel" aria-hidden="true" data-ph-id="ph-page-element-short-header-jt9mae-ef1wbC"></i> </button>
#       </div>
#      </div>
#     </div>
#    </div>
#    <div class="top-header main-nav" data-ph-id="ph-page-element-short-header-jt9mae-0SueD6">
#     <div class="container" data-ph-id="ph-page-element-short-header-jt9mae-4rkQDh">
#      <div class="nav-block" data-ph-id="ph-page-element-short-header-jt9mae-aeW1De">
#       <!-- skip to main content block start-->
#       <p class="skip-nav-para" data-ph-id="ph-page-element-short-header-jt9mae-7ssSOS"> <a href="#acc-skip-content" key-hash-id="short-header-focus_content_text" id="skip-content" ph-tevent="skip_main_content" aria-label="Skip to main content" key-aria-label="short-header-careersSkipContentLabelText" target="_self" key-target="short-header-careersSkipContentTargetValue" class="skip-content au-target" data-ph-id="ph-page-element-short-header-jt9mae-Wt4qqq" hash-id="#content" role="link" au-target-id="11">
#         <ppc-content key="short-header-careersSkipContentLinkText" data-ph-id="ph-page-element-short-header-jt9mae-qUmRdB">
#           Skip to main content
#         </ppc-content> </a> </p>
#       <!-- skip to main content block end-->
#       <nav role="navigation" aria-label="universal" key-aria-label="short-header-universalHeadernavigationLabelTxt" data-ph-id="ph-page-element-short-header-jt9mae-BJ1zX6">
#        <!-- logo block start-->
#        <ul class="main-nav-links main-nav-toggle logo-nav" data-ph-id="ph-page-element-short-header-jt9mae-gJmkAu">
#         <li class="nav-main-link" data-ph-id="ph-page-element-short-header-jt9mae-vnsYNu"> <a ph-tevent="header_menu_click" data-attr="home" data-ph-tevent-attr-trait62="Home" href="https://www.microsoft.com" key-href="short-header-universalHomepageLink" target="_blank" key-target="short-header-universalhomeLogoTargetValue" class="desktop-image au-target" key-aria-label="short-header-universalHomeLogoLabelText" aria-label="Microsoft opens in a new tab" data-ph-id="ph-page-element-short-header-jt9mae-tpT3KM" role="link" au-target-id="12">
#           <ppc-content type="image" aria-hidden="true" data-ph-id="ph-page-element-short-header-jt9mae-GAMqzr">
#            <img src="https://prodcmscdn.azureedge.net/careerconnectresources/p/MICRUS/en_us/desktop/assets/images/microsoft-gray.png" key-src="short-header-universalLogoImg" alt="Microsoft" key-alt="short-header-universalHomeLogoAltText" class="img-responsive" data-ph-id="ph-page-element-short-header-jt9mae-c8nnCi">
#           </ppc-content> </a> </li>
#        </ul>
#        <!-- logo block end -->
#        <!-- mobile toggle menu srart -->
#        <ul class="main-nav-links main-nav-toggle logo-nav" data-ph-id="ph-page-element-short-header-jt9mae-IbjGC3">
#         <li role="presentation" class="show-icon" data-ph-id="ph-page-element-short-header-jt9mae-4ROWAP"> <button onfocus="ph$Msft$Custom.header_mobileButtons_onFocus(this)" onclick="ph$Msft$Custom.top_Header_Mobile_Nav(this)" id="btn-menu" role="button" aria-label="Toggle menu" key-aria-label="short-header-universalToggleBtnLabeltext" tip-suggestion="Toggle menu" aria-expanded="false" class="icon icon-menu" data-ph-id="ph-page-element-short-header-jt9mae-GvL58R"> <span class="sr-only" data-ph-id="ph-page-element-short-header-jt9mae-V56G4d">
#            <ppc-content key="short-header-universalToggleBtntext" data-ph-id="ph-page-element-short-header-jt9mae-7wrinx">
#             Toggle menu
#            </ppc-content></span> </button> </li>
#        </ul>
#        <!-- mobile toggle menu end-->
#        <!-- universal header items start -->
#        <ul class="main-nav-links hidden-tab main-header-nav" id="top-navbar" data-ph-id="ph-page-element-short-header-jt9mae-PHUZCC">
#         <li data-ph-id="ph-page-element-short-header-jt9mae-NafYhg"> <a role="link" ph-tevent="header_menu_click" data-ph-tevent-attr-trait62="Office" class="menu-item topheader-nav au-target" href="https://products.office.com/en-us/home" key-href="short-header-newUniversalOfficeLinkUrl" target="_blank" key-target="short-header-newUniversalOfficeLinkTargetValue" aria-label="Office opens in a new tab" key-aria-label="short-header-newUniversalOfficeLinkLabelText" data-ph-id="ph-page-element-short-header-jt9mae-LbmsNs" au-target-id="13">
#           <ppc-content key="short-header-newUniversalOfficeLinkText" data-ph-id="ph-page-element-short-header-jt9mae-D3jSmr">
#            Office
#           </ppc-content></a> </li>
#         <li data-ph-id="ph-page-element-short-header-jt9mae-rHC9iD"> <a role="link" ph-tevent="header_menu_click" ddata-ph-tevent-attr-trait62="Windows" class="menu-item topheader-nav au-target" href="https://www.microsoft.com/en-us/windows/" key-href="short-header-newUniversalWindowsLinkUrl" aria-label="Windows opens in a new tab" key-aria-label="short-header-newUniversalWindowsLinkLabelText" target="_blank" key-target="short-header-newUniversalWindowsTargetValue" data-ph-id="ph-page-element-short-header-jt9mae-2Rw4dh" au-target-id="14">
#           <ppc-content key="short-header-newUniversalWindowsLinkText" data-ph-id="ph-page-element-short-header-jt9mae-InEdiA">
#            Windows
#           </ppc-content></a> </li>
#         <li data-ph-id="ph-page-element-short-header-jt9mae-RemWtm"> <a role="link" ph-tevent="header_menu_click" data-ph-tevent-attr-trait62="Microsoft Surface deals" class="menu-item topheader-nav au-target" href="https://www.microsoft.com/en-us/surface" key-href="short-header-newUniversalSurfaceDealsLinkUrl" target="_blank" key-target="short-header-newUniversalSurfaceDealsTargetValue" aria-label="Surface deals opens in a new tab" key-aria-label="short-header-newUniversalSurfaceDealsLinkLabelText" data-ph-id="ph-page-element-short-header-jt9mae-VX5OCP" au-target-id="15">
#           <ppc-content key="short-header-newUniversalSurfaceDealsLinkText" data-ph-id="ph-page-element-short-header-jt9mae-NdZrPX">
#            Surface
#           </ppc-content></a> </li>
#         <li data-ph-id="ph-page-element-short-header-jt9mae-VZGorc"> <a role="link" ph-tevent="header_menu_click" data-ph-tevent-attr-trait62="Xbox" class="menu-item topheader-nav au-target" href="https://www.xbox.com/" key-href="short-header-newUniversalXboxLinkUrl" target="_blank" key-target="short-header-newUniversalXboxTargetValue" aria-label="Xbox opens in a new tab" key-aria-label="short-header-newUniversalXboxLinkLabelText" data-ph-id="ph-page-element-short-header-jt9mae-4oFi1i" au-target-id="16">
#           <ppc-content key="short-header-newUniversalXboxLinkText" data-ph-id="ph-page-element-short-header-jt9mae-Kf92Si">
#            Xbox
#           </ppc-content></a> </li>
#         <li data-ph-id="ph-page-element-short-header-jt9mae-7sU8NV"> <a role="link" ph-tevent="header_menu_click" data-ph-tevent-attr-trait62="Deals" class="menu-item topheader-nav au-target" href="https://www.microsoft.com/en-us/store/b/sale?icid=gm_nav_L0_salepage" key-href="short-header-newUniversalDealsLinkUrl" target="_blank" key-target="short-header-newUniversalDealsTargetValue" aria-label="Deals opens in a new tab" key-aria-label="short-header-newUniversalDealsLinkLabelText" data-ph-id="ph-page-element-short-header-jt9mae-qDteTU" au-target-id="17">
#           <ppc-content key="short-header-newUniversalDealsLinkText" data-ph-id="ph-page-element-short-header-jt9mae-1y85iu">
#            Deals
#           </ppc-content></a> </li>
#         <li data-ph-id="ph-page-element-short-header-jt9mae-eWHVCB"> <a role="link" ph-tevent="header_menu_click" onfocus="ph$Msft$Custom.header_mainAnchors_onFocus(this)" data-ph-tevent-attr-trait62="Support" href="https://support.microsoft.com/en-us" key-href="short-header-newUniversalSupportLinkUrl" target="_blank" key-target="short-header-newUniversalSupportTargetValue" aria-label="Support opens in a new tab" key-aria-label="short-header-newUniversalSupportLinkLabeltext" data-ph-id="ph-page-element-short-header-jt9mae-Qleg59" class="au-target" au-target-id="18">
#           <ppc-content key="short-header-newUniversalSupportLinktext" data-ph-id="ph-page-element-short-header-jt9mae-VJ5hCC">
#            Support
#           </ppc-content></a> </li>
#        </ul>
#        <!-- universal header items end -->
#       </nav>
#      </div>
#     </div>
#    </div>
#    <!--top-header end-->
#    <nav role="navigation" class="main-nav" aria-label="careers" key-aria-label="short-header-careersHeaderNavigationLabel" data-ph-id="ph-page-element-short-header-jt9mae-S8mmWV">
#     <div class="container" data-ph-id="ph-page-element-short-header-jt9mae-cUVyIb">
#      <div class="nav-block" data-ph-id="ph-page-element-short-header-jt9mae-94vjUL">
#       <ul class="main-nav-links main-nav-toggle" data-ph-id="ph-page-element-short-header-jt9mae-XwGtAY">
#        <li class="nav-main-link" data-ph-id="ph-page-element-short-header-jt9mae-Zi20gs">
#         <!-- careers header toggle button start--> <button id="main-navigation" onfocus="ph$Msft$Custom.header_mobileButtons_onFocus(this)" class="mobile-btn" aria-expanded="false" aria-label="Careers" key-aria-label="short-header-careersHomepagebtnLabelText" onclick="ph$Msft$Custom.second_Header_Mobile_Nav(this)" data-ph-id="ph-page-element-short-header-jt9mae-hybAYO">
#          <ppc-content key="short-header-careersHomepagebtnText" data-ph-id="ph-page-element-short-header-jt9mae-VTcg9k">Careers</ppc-content><i class="icon icon-down-arrow" aria-hidden="true" data-ph-id="ph-page-element-short-header-jt9mae-8phHzq"></i></button>
#         <!-- careers header toggle button end -->
#         <!-- careers home link start--> <a role="link" onfocus="ph$Msft$Custom.header_mainAnchors_onFocus(this)" key-aria-label="short-header-careersHomepagelinkLabelText" ph-tevent="header_menu_click" data-ph-tevent-attr-trait62="Careers" key-target="short-header-careersHomepageTargetValue" target="_self" key-ph-href="short-header-careersHomepagelinkUrl" aria-label="Careers" class="desktop-btn au-target" data-ph-id="ph-page-element-short-header-jt9mae-J0Xmxr" au-target-id="19" href="/" data-ph-href="/">
#          <ppc-content key="short-header-careersHomepagelinkText" data-ph-id="ph-page-element-short-header-jt9mae-7W5y81">Careers</ppc-content></a>
#         <!-- careers home link end--> </li>
#        <li data-ph-id="ph-page-element-short-header-jt9mae-0AZ1hz" class="hide">
#         <!-- header left scroll btn start--> <button role="button" id="right-scroll" aria-label="Left side overflow scroll" key-aria-label="short-header-showPreviousMenuOptionsText" class="nav-arrow-left hide" onclick="ph$Msft$Custom.header_overFlow_menu_left()" data-ph-id="ph-page-element-short-header-jt9mae-uaolef"> <i class="icon icon-left-arrow" aria-hidden="true" data-ph-id="ph-page-element-short-header-jt9mae-2k84da"></i> </button>
#         <!-- header left scroll btn end--> </li>
#       </ul>
#       <div class="nav-container" data-ph-id="ph-page-element-short-header-jt9mae-SQzrrD">
#        <!-- careers header main menus and links-->
#        <div class="over-flow-container" data-ph-id="ph-page-element-short-header-jt9mae-DZDOoO">
#         <ul class="main-nav-links main-nav-links-block hidden-xs" id="mobiletab" data-ph-id="ph-page-element-short-header-jt9mae-zMjGkt" style="margin-left: -10px;">
#          <li class="menubtn" data-ph-id="ph-page-element-short-header-jt9mae-NzJuOw"> <a role="link" onfocus="ph$Msft$Custom.header_mainAnchors_onFocus(this)" ph-tevent="header_menu_click" data-ph-tevent-attr-trait62="Careers" class="mobile-btn au-target" key-ph-href="short-header-careersMobilehomepageLinkUrl" href="/" aria-label="Home" key-target="short-header-careersMobilehomepageTargetValue" target="_self" key-aria-label="short-header-careersMobilehomepagelabelText" data-ph-id="ph-page-element-short-header-jt9mae-VUWpOJ" au-target-id="20" data-ph-href="/">
#            <ppc-content key="short-header-careersMobilehomepageLinkText" data-ph-id="ph-page-element-short-header-jt9mae-pr7ryv">Home</ppc-content></a> </li>
#          <li is-prof="true" data-ph-id="ph-page-element-short-header-jt9mae-ne50sd"> <button onfocus="ph$Msft$Custom.header_mainButtons_onFocus(this)" onclick="ph$Msft$Custom.second_Header_Mainnav(this)" aria-expanded="false" class="menubtn secondheader-nav" aria-label="Professionals" key-aria-label="short-header-careersProfessionalsPersonaBtnLableText" id="prof-navigation" data-ph-id="ph-page-element-short-header-jt9mae-jWoQmQ">
#            <ppc-content key="short-header-careersProfessionalsPersonaBtnText" data-ph-id="ph-page-element-short-header-jt9mae-elXcxB">
#            Professionals
#           </ppc-content><i class="icon icon-down-arrow header-arrow" aria-hidden="true" data-ph-id="ph-page-element-short-header-jt9mae-gjah5m"></i></button>
#           <ul class="menupanel" aria-labelledby="prof-navigation" data-ph-id="ph-page-element-short-header-jt9mae-xXjHIO">
#            <li data-ph-id="ph-page-element-short-header-jt9mae-xIpvEb"> <a role="link" key-ph-href="short-header-careersProfessionsHomeLinkUrl" key-target="short-header-careersProfessionsHomeTargetValue" target="_self" ph-tevent="header_menu_click" data-ph-tevent-attr-trait62="Professions Home" class="menubtn au-target" aria-label="Home" key-aria-label="short-header-careersProfessionsHomeLinkLabelText" data-ph-id="ph-page-element-short-header-jt9mae-jRBNPe" au-target-id="21" href="/professionals/us/en" data-ph-href="/professionals/us/en">
#              <ppc-content key="short-header-careersProfessionsHomeLinkText" data-ph-id="ph-page-element-short-header-jt9mae-0hNKT7" language-overriden="true">Home</ppc-content></a> </li>
#            <li data-ph-id="ph-page-element-short-header-jt9mae-4J3XYN"> <a role="link" key-ph-href="short-header-careersLocationsLinkUrl" key-target="short-header-careersLocationsTargetValue" target="_self" ph-tevent="header_menu_click" data-ph-tevent-attr-trait62="Locations" class="menubtn au-target" aria-label="Locations" key-aria-label="short-header-careersLocationsLinkLabelText" data-ph-id="ph-page-element-short-header-jt9mae-m7jDXR" au-target-id="22" href="/professionals/us/en/locations" data-ph-href="/professionals/us/en/locations">
#              <ppc-content key="short-header-careersLocationsLinkText" data-ph-id="ph-page-element-short-header-jt9mae-std8UZ">Locations</ppc-content></a> </li>
#            <li data-ph-id="ph-page-element-short-header-jt9mae-eam2tG"> <a role="link" key-target="short-header-careersProfessionsTargetValue" target="_self" key-ph-href="short-header-careersProfessionsLinkUrl" ph-tevent="header_menu_click" data-ph-tevent-attr-trait62="Professions" id="Pro-navigation" class="menubtn au-target" aria-label="Professions" key-aria-label="short-header-careersProfessionsLinkLabelText" data-ph-id="ph-page-element-short-header-jt9mae-F1I00a" au-target-id="23" href="/professionals/us/en/professions" data-ph-href="/professionals/us/en/professions">
#              <ppc-content key="short-header-careersProfessionsLinkText" data-ph-id="ph-page-element-short-header-jt9mae-fGPCEr">Professions</ppc-content></a> </li>
#           </ul> </li>
#          <li data-ph-id="ph-page-element-short-header-jt9mae-RkSIw0"> <a role="link" key-ph-href="short-header-careersStudentsPersonaLinkUrl" onfocus="ph$Msft$Custom.header_mainAnchors_onFocus(this)" key-target="short-header-careersStudentsPersonaTargetValue" target="_self" ph-tevent="header_menu_click" data-ph-tevent-attr-trait62="Students and graduates" id="students-navigation" class="menubtn au-target" aria-label="Students and graduates" key-aria-label="short-header-careersStudentsPersonaLinkLabelText" data-ph-id="ph-page-element-short-header-jt9mae-DrE9C7" au-target-id="24" href="/students/us/en" data-ph-href="/students/us/en">
#            <ppc-content key="short-header-careersStudentsPersonaLinkText" data-ph-id="ph-page-element-short-header-jt9mae-GB9KPg">
#            Students and graduates
#           </ppc-content></a> </li>
#          <li data-ph-id="ph-page-element-short-header-jt9mae-aDaLo1"> <button onfocus="ph$Msft$Custom.header_mainButtons_onFocus(this)" onclick="ph$Msft$Custom.second_Header_Mainnav(this)" aria-expanded="false" class="menubtn secondheader-nav" aria-label="Life at Microsoft" key-aria-label="short-header-careersLamLableText" id="Lam-navigation" data-ph-id="ph-page-element-short-header-jt9mae-T1SE7U">
#            <ppc-content key="short-header-careersLamBtnText" data-ph-id="ph-page-element-short-header-jt9mae-M3Juax">Life at Microsoft</ppc-content><i class="icon icon-down-arrow header-arrow" aria-hidden="true" data-ph-id="ph-page-element-short-header-jt9mae-GEhfYf"></i></button>
#           <ul class="menupanel" aria-labelledby="Lam-navigation" data-ph-id="ph-page-element-short-header-jt9mae-8OnQx0">
#            <li data-ph-id="ph-page-element-short-header-jt9mae-SJWOZD"> <a aria-label="Benefits" key-aria-label="short-header-careersBenefitsLinkLableText" ph-tevent="header_menu_click" data-ph-tevent-attr-trait62="Benefits" key-target="short-header-careersBenefitsTargetValue" target="_self" role="link" class="menu-item secondheader-nav au-target" key-ph-href="short-header-careersBenefitsLinkUrl" data-ph-id="ph-page-element-short-header-jt9mae-d9xT7d" au-target-id="25" href="/us/en/benefits" data-ph-href="/us/en/benefits">
#              <ppc-content key="short-header-careersBenefitsLinkText" data-ph-id="ph-page-element-short-header-jt9mae-oBm7Ek">Benefits</ppc-content></a> </li>
#            <li data-ph-id="ph-page-element-short-header-jt9mae-HPxuC9"> <a role="link" ph-tevent="header_menu_click" data-ph-tevent-attr-trait62="Culture" class="menu-item secondheader-nav au-target" key-target="short-header-careersCultureTargetValue" target="_self" key-ph-href="short-header-careersCultureLinkUrl" aria-label="Culture" key-aria-label="short-header-careersCultureLinkLabelText" data-ph-id="ph-page-element-short-header-jt9mae-eMXPG6" au-target-id="26" href="/us/en/culture" data-ph-href="/us/en/culture">
#              <ppc-content key="short-header-careersCultureLinkText" data-ph-id="ph-page-element-short-header-jt9mae-I9tHZP">Culture</ppc-content></a> </li>
#            <li data-ph-id="ph-page-element-short-header-jt9mae-Z0nhAR"> <a aria-label="Diversity and inclusion" key-aria-label="short-header-careersDandILinkLabelText" ph-tevent="header_menu_click" data-ph-tevent-attr-trait62="Diversity and inclusion" key-target="short-header-areersDandITargetValue" target="_self" role="link" class="menu-item secondheader-nav au-target" key-ph-href="short-header-careersDandILinkUrl" data-ph-id="ph-page-element-short-header-jt9mae-YNoZMG" au-target-id="27" href="/us/en/diversityandinclusion" data-ph-href="/us/en/diversityandinclusion">
#              <ppc-content key="short-header-careersDandILinkText" data-ph-id="ph-page-element-short-header-jt9mae-4aXakq">Diversity and inclusion</ppc-content></a> </li>
#            <li data-ph-id="ph-page-element-short-header-jt9mae-bo4PRm"> <a aria-label="US Military &amp; Veterans" key-aria-label="short-header-careersUsMandVLinkLabelText" ph-tevent="header_menu_click" data-ph-tevent-attr-trait62="U.S. Military and Veterans" key-target="short-header-careersUsMandVTargetValue" target="_self" role="link" class="menu-item secondheader-nav au-target" key-ph-href="short-header-careersUsMandVLinkUrl" data-ph-id="ph-page-element-short-header-jt9mae-FGdw7h" au-target-id="28" href="/us/en/military" data-ph-href="/us/en/military">
#              <ppc-content key="short-header-careersUsMandVLinkText" data-ph-id="ph-page-element-short-header-jt9mae-q3iDDF">US Military &amp; Veterans</ppc-content></a> </li>
#            <li data-ph-id="ph-page-element-short-header-jt9mae-cEYucc"> <a aria-label="Microsoft Life opens in a new tab" key-aria-label="short-header-careersMsftLifeLinkLabelText" ph-tevent="header_menu_click" data-ph-tevent-attr-trait62="Microsoft Life" class="menu-item secondheader-nav au-target" href="https://news.microsoft.com/life/" key-href="short-header-careersMsftLifeLinkUrl" target="_blank" key-target="short-header-careersMsftLifeTargetValue" data-ph-id="ph-page-element-short-header-jt9mae-Yds5x2" role="link" au-target-id="29">
#              <ppc-content key="short-header-careersMsftLifeLinkText" data-ph-id="ph-page-element-short-header-jt9mae-sSZhub">Microsoft Life</ppc-content></a> </li>
#           </ul> </li>
#          <!-- <li>
#                                         <a role="link" ph-href="locations" key-ph-href="careersLocationsLinkUrl" key-target="careersLocationsTargetValue" target="_self" onfocus="ph$Msft$Custom.header_mainAnchors_onFocus(this)" ph-tevent="header_menu_click" data-ph-tevent-attr-trait62="Locations" class="menubtn" aria-label="Locations" key-aria-label="careersLocationsLinkLabelText"><ppc-content key="careersLocationsLinkText">Locations</ppc-content></a>
#                                     </li> -->
#          <!-- <li>
#                                         <a role="link" ph-href="search-results" key-ph-href="careersSearchJobsLinkUrl" onfocus="ph$Msft$Custom.header_mainAnchors_onFocus(this)" ph-tevent="header_menu_click" data-ph-tevent-attr-trait62="Search jobs" id="search-jobs-link" class="menubtn" aria-label="Search jobs" key-aria-label="careersSearchJobsLinkLabelText"><ppc-content key="careersSearchJobsLinkText">Search jobs</ppc-content></a>
#                                     </li> -->
#          <!-- <li role="presentation">
#                                         <button onfocus="ph$Msft$Custom.header_mainButtons_onFocus(this)" onclick="ph$Msft$Custom.second_Header_Mainnav(this)" aria-expanded="false" class="menubtn secondheader-nav" aria-label="Search jobs" key-aria-label="careersSearchJobsLinkLabelText" id="sj-navigation"><ppc-content key="careersSearchJobsLinkText">Search jobs</ppc-content><i class="icon icon-down-arrow header-arrow" aria-hidden="true"></i></button>
#                                         <ul class="menupanel" aria-labelledby="sj-navigation">
#                                             <li>
#                                                 <a aria-label="Experienced professionals" key-aria-label="careersExperiencedprofessionalsLinkLabelText" ph-tevent="header_menu_click" key-target="careersExperiencedprofessionalsTargetValue" target="_self" data-ph-tevent-attr-trait62="Experienced professionals" role="link" class="menu-item secondheader-nav" ph-href="search-results" key-ph-href="careersExperiencedprofessionalsLinkUrl"><ppc-content key="careersExperiencedprofessionalsLinkText">Experienced professionals</ppc-content></a>
#                                             </li>
#                                             <li>
#                                                 <a role="link" ph-tevent="header_menu_click" data-ph-tevent-attr-trait62="Students and recent graduates" class="menu-item secondheader-nav" key-target="careersStudentsAndRecentGraduatesTargetValue" target="_self" ph-href="search-results?rt=university" key-ph-href="careersStudentsAndRecentGraduatesLinkUrl" aria-label="Students and recent graduates" key-aria-label="careersStudentsAndRecentGraduatesLinkLabelText"><ppc-content key="careersStudentsAndRecentGraduatesLinkText">Students and recent graduates</ppc-content></a>
#                                             </li>
#                                         </ul>
#                                     </li> -->
#          <!-- <li>
#                                         <a role="link" onfocus="ph$Msft$Custom.header_mainAnchors_onFocus(this)" href="https://careers.linkedin.com/" key-href="careersWalLinkUrl" ph-tevent="header_menu_click" data-ph-tevent-attr-trait62="Working at LinkedIn" target="_blank" key-target="careersWalcareers" class="menubtn" aria-label="Working at LinkedIn opens in a new tab" id="linkedin-link-id" key-aria-label="careersWalLinkLabelText"><ppc-content key="careersWalLinkText">Working at LinkedIn</ppc-content></a>
#                                     </li> -->
#          <!-- <li>
#                                         <a ph-tevent="header_menu_click" key-ph-href="careersReferralsLinkUrl" data-ph-tevent-attr-trait62="Referrals" class="menubtn hide" role="link" target="_blank" key-target="careersReferralsTargetValue" id="referal-link-tab" ph-href="referrals" aria-label="Referrals opens in a new tab" key-aria-label="careersReferralsLinkLabelText">
#                                             <ppc-content key="careersReferralsLinkText">Referrals</ppc-content>
#                                         </a>
#                                     </li> -->
#         </ul>
#        </div>
#        <!-- careers header main menus and links end -->
#        <!-- log in and saved jobs widgets start -->
#        <div class="right-actions" data-ph-id="ph-page-element-short-header-jt9mae-IoDg0I">
#         <section class="ph-widget ppc-section ph-widget-layout" instance-id="z5b0az" data-ph-id="ph-page-element-short-header-jt9mae-YICFLn">
#          <div as-element="ph-oauthsignin-v1" data-widget="ph-oauthsignin-v1" class="ph-oauthsignin-v1-my-profile-default ph-widget-target au-target" view="1559835047040-my-profile" mode="myProfile" instance-id="z5b0az" data-ph-id="ph-page-element-short-header-jt9mae-b8O6Kr" original-view="my-profile" au-target-id="30">
#
#                                     <button role="button" aria-label="Right side overflow scroll" key-aria-label="z5b0az-parent-jt9mae-ph-oauthsignin-v1-my-profile-showNextMenuOptionsLabelText" class="nav-arrow-right show-arrow" onclick="ph$Msft$Custom.header_overFlow_menu_right()" data-ph-id="ph-page-element-short-header-z5b0az-y2fvAD">
#                                         <i class="icon icon-arrow-right" aria-hidden="true" data-ph-id="ph-page-element-short-header-z5b0az-7CCtjP"></i>
#                                     </button>
#                                     <span data-ph-id="ph-page-element-short-header-z5b0az-lnyOMs">
#                                         <button role="button" id="sign-profile" onfocus="ph$Msft$Custom.header_mainAnchors_onFocus(this);ph$Msft$Custom.header_signinAnchor_onFocus();" ph-tevent="signIn_click" click.delegate="handlePagePath($event, 'login')" aria-label="Sign in" class="btn primary-button au-target" key-aria-label="z5b0az-parent-jt9mae-ph-oauthsignin-v1-my-profile-careersSignInLinkLabelText" data-ph-id="ph-page-element-short-header-z5b0az-pI3nJq" au-target-id="101">
#                                             <p data-ph-id="ph-page-element-short-header-z5b0az-d27CFv"><ppc-content key="z5b0az-parent-jt9mae-ph-oauthsignin-v1-my-profile-careersSignInLinkText" data-ph-id="ph-page-element-short-header-z5b0az-GaDFa0">Sign in</ppc-content></p>
#                                         </button>
#                                     </span><!--anchor-->
#                                     <!--anchor-->
#                                 <!--anchor--></div>
#         </section>
#         <section class="ph-widget ppc-section ph-widget-layout" instance-id="u6t44s" data-ph-id="ph-page-element-short-header-jt9mae-L6RZM0">
#          <div as-element="ph-job-cart-count-v3" class="ph-job-cart-count-v3-view1-default ph-widget-target au-target" view="1559835047050-view1" data-widget="ph-job-cart-count-v3" instance-id="u6t44s" data-ph-id="ph-page-element-short-header-jt9mae-YYNmEF" original-view="view1" au-target-id="31">
#
#                                     <a key-ph-href="u6t44s-parent-jt9mae-ph-job-cart-count-v3-view1-careersSavedJobsLinkUrl" class="phs-job-cart-area au-target" ph-tevent="job-cart-icon-click" onfocus="ph$Msft$Custom.header_mainAnchors_onFocus(this)" tip-suggestion="Saved jobs" data-ph-at-id="jobcart-count" data-ph-id="ph-page-element-short-header-u6t44s-bqZC0I" au-target-id="115" href="/us/en/savedjobs" data-ph-href="/us/en/savedjobs" aria-label="Saved jobs " data-ph-at-widget-data-count="0">
#                                         <ppc-content type="icon" data-ph-id="ph-page-element-short-header-u6t44s-gOoRzb">
#                                             <i aria-hidden="true" data-ph-id="ph-page-element-short-header-u6t44s-ShS36W" class="au-target icon icon-star-empty" au-target-id="116"></i>
#                                         </ppc-content>
#                                         <span class="savedJobsText" data-ph-id="ph-page-element-short-header-u6t44s-R993qp">
#                                             <ppc-content key="u6t44s-parent-jt9mae-ph-job-cart-count-v3-view1-careersSavedJobsLinkText" data-ph-at-id="heading-text" data-ph-id="ph-page-element-short-header-u6t44s-aHSv3w">Saved jobs</ppc-content>
#                                         </span>
#                                         <span data-ph-id="ph-page-element-short-header-u6t44s-2lQHXe" class="au-target phs-jobcart-count hide" au-target-id="117">0</span>
#                                     </a>
#                                 <!--anchor--></div>
#         </section>
#        </div>
#        <!-- log in and saved jobs widgets end -->
#       </div>
#      </div>
#     </div>
#    </nav>
#   </header>
#  </div>
# </div></section></div>
#   <div class="ph-page" role="main" data-ph-id="ph-page-element-page19-Qwutdi"><div class="skiptarget"><a id="acc-skip-content" aria-hidden="true" role="link">-</a></div><h1 class="sr-only">Search results</h1>
#    <!--<h1 class="sr-only" tab-index="-1">Search results</h1>-->
#    <div class="body-wrapper ph-page-container" data-ph-id="ph-page-element-page19-527utw">
#     <!--End skip landing area block-->
#     <!-- <h1 class="sr-only"><ppc-content key="searchPageHeadingLevel11TitleText">Search results</ppc-content></h1> -->
#     <div class="container" data-ph-id="ph-page-element-page19-Iby7eJ">
#      <!-- Global Search block-->
#      <div class="search-container" data-ph-id="ph-page-element-page19-vz9jKy">
#       <section class="ph-widget" instance-id="p3mrzw" view="p3mrzw-default" original-view="default" data-ph-id="ph-page-element-page19-FF8cOz">
#        <div as-element="ph-global-search-v3" reload-on-clear.bind="true" class="ph-global-search-v3-default-default ph-widget-target au-target" data-widget="ph-global-search-v3" show-title.bind="false" placeholder-text.bind="'Job title or location'" arrow-navigation.bind="false" instance-id="p3mrzw" view="default-1566408052426" original-view="default" data-ph-id="ph-page-element-page19-ibrjsC" au-target-id="32">
#
#                                     <form class="phs-global-search-area ph-widget-box au-target" aria-label="Find jobs" key-aria-label="p3mrzw-ph-global-search-v3-default-homeGlobalsearchFormAriaLabel" keyup.delegate="arrowKeyUp($event)" novalidate="" action="" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-fdlAOn" au-target-id="119">
#                                         <div class="search-text-block" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-Ajdiqe">
#                                             <!-- <h1 if.bind="showTitle">
#                                                 <ppc-content key="homeGlobalsearchHeading1doWhatYouLoveText" data-ph-at-id="widget-heading-text">Do what you love</ppc-content>
#                                             </h1> -->
#                                             <!-- <p if.bind="showCaption">
#                                                 <ppc-content key="searchJobsHeading">Search jobs</ppc-content>
#                                             </p>                                         -->
#                                         </div>
#                                         <!-- <div class="short-ratio-btn-group">
#                                             <p>
#                                                 <ppc-content key="chooseOpportunityText">Opportunity type:</ppc-content>
#                                             </p>
#                                             <div class="raio-btn-block">
#                                                 <label class="inpu-radio-group">
#                                                     <input type="radio" value="professional" checked.bind="selectedReqType" name="experiencedreqtype" id="professional_radio" aria-label="Experienced professionals">
#                                                     <span class="radio-seletced"></span>
#                                                     <span class="radio-text">
#                                                         <ppc-content key="homeGlobalsearchHeading1ProfessionalLabelText">Experienced
#                                                             professionals</ppc-content>
#                                                     </span>
#                                                 </label>
#                                             </div>
#                                             <div class="raio-btn-block">
#                                                 <label class="inpu-radio-group">
#                                                     <input type="radio" value="university" checked.bind="selectedReqType" name="studentsreqtype" id="university_radio" aria-label="Students and recent graduates">
#                                                     <span class="radio-seletced"></span>
#                                                     <span class="radio-text">
#                                                         <ppc-content key="homeGlobalsearchHeading1StudentsLabelText">Students
#                                                             and recent graduates</ppc-content>
#                                                     </span>
#                                                 </label>
#                                             </div>
#                                         </div> -->
#                                         <div class="form-group" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-PYXVY7">
#                                             <div class="input-group row" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-4YN3jm">
#                                                 <div class="col-xs-10" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-WJdU9r">
#                                                     <div class="job-filter ph-suggestion-focus-block" data-ph-at-id="keyword-category-location" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-0QtpB2">
#                                                         <input id="searchBox" type="text" name="phsKeywords" focus.trigger="handleFocus($event)" blur.trigger="gsClrTxt = 0" key-placeholder="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeadingPlaceholderText" ref="phGSearchInput" aria-label="Search jobs" key-aria-label="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeadingSearchLinkAriaLabelText" onkeydown="arrowacce$$List(event)" placeholder="Search jobs" class="form-control phs-keywords input-lg au-target" value.bind="searchValue &amp; debounce:100" maxlength="200" autocomplete="off" data-ph-at-id="globalsearch-input" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-Jr4Lqz" au-target-id="120">
#                                                         <span class="search-sym" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-uUs5bF">
#                                                             <ppc-content type="icon" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-gTGRWv">
#                                                                 <i class="icon icon-search" aria-hidden="true" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-ZOvdLi"></i>
#                                                             </ppc-content>
#                                                         </span>
#                                                         <div class="clear-block" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-Ck6tyj">
#                                                             <button data-ph-at-id="clear-globalsearch-link" type="button" keyup.trigger="gsClrTxt = 1" mouseup.trigger="gsClrTxt = 1" ph-tevent="clear_searches_click" class="phs-keysearch-clear au-target" role="button" click.trigger="clearSearch($event)" onclick="setTimeout(function(){document.getElementById('searchBox').focus(); gsClrTxt = 0},500)" show.bind="searchValue" href="javascript:void(0)" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-l5RzZA" au-target-id="121">
#                                                                 <ppc-content type="icon" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-wNgHsj">
#                                                                     <i class="icon icon-cancel" aria-hidden="true" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-VxD3sn"></i>
#                                                                 </ppc-content>
#                                                                 <span class="sr-only" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-eC1C0E">
#                                                                     <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1OffScreenReaderClearText" data-ph-at-id="clear-globalsearch-text" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-AYQLrZ">
#            Clear text
#           </ppc-content>
#                                                                 </span>
#                                                             </button>
#                                                         </div>
#                                                         <!--anchor-->
#                                                     </div>
#                                                 </div>
#                                                 <div class="col-xs-2" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-utlBcv">
#                                                     <span class="input-group-btn" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-KYdeFT">
#                                                         <button type="button" role="button" data-ph-at-id="globalsearch-button" click.delegate="handleSubmitClick({'checkValidation': false})" class="btn primary-button btn-lg phs-search-submit au-target" aria-label="Find jobs" key-aria-label="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1FindjobsBtnAriaLabelText" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-7HDrYh" au-target-id="192">
#                                                             <ppc-content type="icon" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-IRMaNH">
#                                                                 <i class="icon icon-search" aria-hidden="true" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-Cse1mR"></i>
#                                                             </ppc-content>
#                                                             <span data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-rUJPN7">
#                                                                 <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGlobalsearchHeading1FindjobsBtnText" data-ph-at-id="globalsearch-button-text" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-V5Dmhc">
#           Find jobs
#          </ppc-content>
#                                                             </span>
#                                                         </button>
#                                                     </span>
#                                                 </div>
#                                             </div>
#                                         </div>
#                                     </form>
#                                     <div class="sr-only" aria-live="assertive" aria-atomic="true" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-zXMDoo">
#                                         <!--anchor-->
#                                     </div>
#                                     <div class="sr-only" aria-live="assertive" aria-atomic="true" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-bI2dHK">
#                                         <!--anchor-->
#                                         <span data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-jOg2SA">
#                                             <ppc-content key="p3mrzw-ph-global-search-v3-default-homeGSHeading1OffScreenNoSuggestionsNeText" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-E6mY5y">No suggestions available</ppc-content>
#                                         </span><!--anchor-->
#                                     </div><!--anchor-->
#                                     <!-- <div class="sr-only" aria-live="assertive" aria-atomic="true">
#                                         <span if.bind="!showDropDown && !searchValue.length"><ppc-content key="homeGlobalsearchHeading1OffScreenCollapsedText">Collapsed</ppc-content></span>
#                                     </div> -->
#                                     <!-- Live region start -->
#                                     <!-- <span aria-live="assertive" aria-atomic="true" class="sr-only">
#                                         <span if.bind="showDropDown && showAllJobCategories && !searchValue.length">
#                                             <ppc-content key="homeGlobalsearchHeading1OffScreenSelectProfessionText">Use tab or up and down arrows keys to access profession. Expanded</ppc-content>
#                                         </span>
#                                     </span> -->
#                                     <!-- Live region end -->
#
#                                     <!-- Keyword search information -->
#                                     <div class="learn-keyword-search-block" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-dX81c3"><button onclick="keyword$SearchInfo$(this,true)" aria-label="click on this to view more info" class="learn-more-info-btn" tool-tip="Learn more about search  jobs" key-tool-tip="p3mrzw-ph-global-search-v3-default-globalSearchLearnMoreKeywordsSearchBtToolTipText" key-aria-label="p3mrzw-ph-global-search-v3-default-globalSearchLearnMoreKeywordsSearchBtnAriaLabelTextText" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-oSGw2v"><i class="icon icon-info-o" aria-hidden="true" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-6aq0zR"></i><span data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-0HG88K"><ppc-content key="p3mrzw-ph-global-search-v3-default-globalSearchLearnMoreKeywordsSearchBtnText" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-451LuE">Learn more</ppc-content></span></button>
#                                         <div class="learn-more-info hide" role="alert" aria-atomic="false" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-tB8KE6">
#                                             <span id="lear_more_info" class="hide" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-9wdQwx"><span class="learn-info-ext" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-RSjino"><ppc-content key="p3mrzw-ph-global-search-v3-default-globalSearchLearnMoreKeywordsSearchDescInfoExtText" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-zm6D7Z">Start a new search with a keyword or using the filters below. Ideas for your keyword search: job ID, any skill or title, for example C++, AI, or “Program Manager.”</ppc-content></span>
#                                             <span class="learn-info-ext-1" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-IXe2qJ"><ppc-content key="p3mrzw-ph-global-search-v3-default-globalSearchLearnMoreKeywordsSearchDescInfoExtText1" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-OQO5gG">Using double quotations (“”) searches for an exact phrase match.</ppc-content></span>
#                                             </span>
#                                             <span id="lear_more_info_int" class="hide" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-CifyqR"><span class="learn-info-int" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-7tsh2q"><ppc-content key="p3mrzw-ph-global-search-v3-default-globalSearchLearnMoreKeywordsSearchDescInfoIntText" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-j8NbEa">Start a new search with a keyword or using the filters below. Ideas for your keyword search: hiring manager alias, job ID, any skill or title, for example C++, AI, or “Program Manager.”</ppc-content></span>
#                                             <span class="learn-info-int-1" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-98Y2Ac"><ppc-content key="p3mrzw-ph-global-search-v3-default-globalSearchLearnMoreKeywordsSearchDescInfoIntText1" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-QLgNdt">Using double quotations (“”) searches for an exact phrase match.</ppc-content></span></span>
#                                             <button onclick="keyword$SearchInfo$(this,false)" onkeydown="closeLmpopUp(this,event)" class="close-keyword-info" aria-label="close learn more popup" key-aria-label="p3mrzw-ph-global-search-v3-default-globalSearchLearnMoreKeywordsSearchCloseAriaLabelText" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-twde9Z"><i class="icon icon-cancel" aria-hidden="true" data-ph-id="ph-default-1566400319840-ph-global-search-v3p3mrzw-SoLVSr"></i></button>
#                                         </div>
#                                     </div>
#                                 <!--anchor--></div>
#       </section>
#      </div>
#      <!--End Global Search block-->
#      <div class="row" data-ph-id="ph-page-element-page19-TJkYcU">
#       <!-- Left side block -->
#       <div class="col-md-4 col-sm-5 addition-padding" data-ph-id="ph-page-element-page19-R4KWyG">
#        <!-- Search Facets block -->
#        <section class="ph-widget" instance-id="lqzfz5" view="lqzfz5-view-external" original-view="view-external" data-ph-id="ph-page-element-page19-j8JqwM">
#         <div as-element="ph-facets-v1" data-widget="ph-facets-v1" class="ph-facets-v1-view-external-default ph-widget-target au-target" view="view-external-1566561389257" page-size.bind="20" is-error-msg-reqd.bind="true" instance-id="lqzfz5" role="region" aria-labelledby="facet-search-block" original-view="view-external" data-ph-id="ph-page-element-page19-XxXb7O" au-target-id="33">
#
#                                 <div class="phs-refine-block" role="region" aria-labelledby="facet-search-block" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-bog50P">
#                                     <a href="#content" class="skip-block" aria-label="Skip to Show Results" key-aria-label="lqzfz5-ph-facets-v1-view-external-searchFacetsSkipBlockLinkAriaLabelText" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-k6nx4P"><ppc-content key="lqzfz5-ph-facets-v1-view-external-searchFacetsSkipBlockLinkText" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-ckAcok">Skip to Show Results</ppc-content></a>
#                                     <div class="phs-hide-filter" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-mxfH7Y">
#                                         <a href="javascript:void(0)" click.delegate="hideFacetFilter()" aria-label="Close the filter" key-aria-label="lqzfz5-ph-facets-v1-view-external-searchFacetsLinkAriaLabel" tabindex="0" role="button" data-ph-at-id="mobile-facet-filter-close-link" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-5YU1od" class="au-target" au-target-id="198">
#                                             <ppc-content type="icon" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-1niQag">
#                                                 <i class="icon icon-cancel" aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-5CQZ1r"></i>
#                                             </ppc-content>
#                                         </a>
#                                     </div>
#                                     <div class="panel panel-default main-panel" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-xVf303">
#                                         <div class="panel-heading" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-LyUf7J">
#                                             <h2 class="panel-title" id="facet-search-block" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-Sxc1TP">
#                                                 <ppc-content key="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1Text" data-ph-at-id="heading-text" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-mzDgaF">
#          Refine your search
#        </ppc-content>
#                                             </h2>
#                                         </div>
#                                         <div class="panel-heading mobile-toggle-button" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-m379cG">
#                                             <h2 class="panel-title" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-qhbIhx">
#                                                 <button click.delegate="facetKey.refineOpen = !facetKey.refineOpen" aria-label="toggle refine search" key-aria-label="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1BtnAriaLabelText" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-qEcpqE" class="au-target" au-target-id="199" aria-expanded="true">
#                                                     <ppc-content key="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1BtnText" data-ph-at-id="mobile-heading-text" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-ICqwMf">
#           Refine your search
#         </ppc-content>
#                                                     <ppc-content type="icon" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-7TXvJM">
#                                                         <i aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-I87dV0" class="au-target icon icon-down-arrow" au-target-id="200"></i>
#                                                     </ppc-content>
#                                                 </button>
#                                             </h2>
#                                         </div>
#                                     </div>
#                                     <div data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-0BBTbM" class="au-target phs-filter-panels show" au-target-id="201">
#                                         <div class="panel panel-default refine-widget" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-K7McKK">
#                                             <!-- <div class="panel-heading">
#                                                 <span class="panel-title">
#                                                     <button class="facet-menu" click.trigger="facetKey.toggleOpen = !facetKey.toggleOpen" keyup.trigger="($event.keyCode === 27)? (facetKey.toggleOpen = false):''" aria-expanded="${facetKey.toggleOpen ? 'true' : 'false'}" aria-label="Keywords Search" key-aria-label="searchFacetsHeadingLevel1KeywordsSearchBtnAriaLabelText">
#                                                         <ppc-content key="searchFacetsHeadingLevel1KeywordsSearchBtnText" data-ph-at-id="facet-accordian-text">Keywords</ppc-content>
#                                                         <ppc-content type="icon">
#                                                             <i class="${facetKey.toggleOpen ? 'icon icon-up-arrow' : 'icon icon-down-arrow'}" aria-hidden="true"></i>
#                                                         </ppc-content>
#                                                     </button>
#                                                 </span>
#                                             </div> -->
#                                             <div class="panel-collapse collapse in" data-ph-at-id="facet-sub-search" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-UhSosE">
#                                                 <div class="search-container" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-9fwok9">
#                                                     <form data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-XgLI3G">
#                                                         <div class="input-group input-group-sm has-feedback-search" role="search" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-GbyLQK">
#                                                             <!-- <label class="sr-only" aria-hidden="true">
#                                                                 <ppc-content key="searchFacetsHeadingLevel1SearchWithinkeywordsText" data-ph-at-id="sub-search-textbox-text">
#                                                                     Search keywords within results
#                                                                 </ppc-content>
#                                                             </label> -->
#                                                             <input focus.trigger="clrTxt = 0" type="text" value.bind="searchParams.subsearch" placeholder="Search within results" key-placeholder="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1SearchWithinkeywordsPlaceHolderText" autocomplete="off" class="form-control au-target" id="sub_search_textbox" maxlength="200" data-ph-at-id="sub-search-textbox" aria-label="Search within results" key-aria-label="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1SearchWithinkeywordsAriaLabelText" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-Trs4c3" au-target-id="202">
#                                                             <span class="sr-tooltip" aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-c87Tg2"><ppc-content key="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1SearchWithinkeywordstoolTipText" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-p6PNSg">Search within results</ppc-content></span>
#                                                             <!--anchor-->
#                                                             <span class="input-group-btn" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-yklRE6">
#                                                                 <button type="submit" click.delegate="filterSearch()" aria-label="Search" key-aria-label="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1SKWRCSearchSubmitBtnAriaLabelText" role="button" key-role="DNVvxt-lqzfz5-ph-facets-v1-view-external-btnRole" tip-toolinfo="Search jobs" key-tip-toolinfo="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1SKWRCSubmitBtnTooltipText" data-ph-at-id="sub-search-textbox-button" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-oe99im" class="au-target btn btn-default disabled" au-target-id="205">
#                                                                     <i class="icon icon-search" aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-h2QsHV"></i>
#                                                                 </button>
#                                                             </span>
#                                                         </div>
#                                                     </form>
#                                                     <!--anchor-->
#                                                     <!-- <div class="learn-keyword-search-block"><button onclick="keyword$SearchInfo$(this,true)" aria-label="Learn more" class="learn-more-info-btn" key-aria-label="searchFacetsHeadingLevel1LearnMoreKeywordsSearchBtnAriaLabelTextText"><i class="icon icon-info-o" aria-hidden="true"></i><span><ppc-content key="searchFacetsHeadingLevel1LearnMoreKeywordsSearchBtnText">Learn more</ppc-content></span></button>
#                                                         <div class="learn-more-info hide" role="alert">
#                                                             <span id="lear_more_info" if.bind="commonService.getSiteType() != 'internal'"><ppc-content key="searchFacetsHeadingLevel1LearnMoreKeywordsSearchDescInfoText">You can enter multiple keywords with a comma(,) or add separately. You can use keywords and also search by job ID, "remote".</ppc-content></span>
#                                                             <span id="lear_more_info_int" if.bind="commonService.getSiteType() == 'internal'"><ppc-content key="searchFacetsHeadingLevel1LearnMoreKeywordsSearchDescInfoText">You can enter multiple keywords with a comma(,) or add separately. You can use keywords and also search by job ID, "remote", or hiring manager alias.</ppc-content></span>
#                                                             <button onclick="keyword$SearchInfo$(this,false)" class="close-keyword-info" aria-label="close keyword search popup" key-aria-label="searchFacetsHeadingLevel1LearnMoreKeywordsSearchCloseAriaLabelText"><i class="icon icon-cancel" aria-hidden="true"></i></button>
#                                                         </div>
#                                                     </div> -->
#                                                 </div>
#                                             </div>
#
#                                         </div>
#                                         <div class="panel panel-default refine-widget au-target" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-a1seui" au-target-id="207" data-ph-at-id="facet-experience" data-ph-at-text="experience">
#                                             <!-- facet heading { bindings :  facetKey }-->
#                                             <div class="panel-heading" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-hoHIq8">
#                                                 <span class="panel-title" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-deX2cm">
#                                                     <button class="facet-menu au-target" keyup.trigger="($event.keyCode === 27)? (facetKey.visible = false):''" click.delegate="adjustAccordian($index)" data-ph-at-id="facet-heading-link" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-uHxChv" au-target-id="208" aria-label="Experience" aria-expanded="true" data-ph-at-text="Experience">
#                                                         Experience
#                                                         <ppc-content type="icon" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-1z3rWp">
#                                                             <i aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-UcYCva" class="au-target icon icon-up-arrow" au-target-id="210"></i>
#                                                         </ppc-content>
#                                                     </button>
#                                                 </span>
#                                             </div>
#                                             <!-- facet options block -->
#                                             <div class="panel-collapse collapse in" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-nvUI3r">
#                                                 <div class="panel-body" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-B1fXQw">
#                                                     <!-- search field and button -->
#                                                     <!--anchor-->
#                                                     <div class="sr-only" aria-relevant="additions text" aria-label="Text cleared" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-QSmuSF">
#                                                         <!--anchor-->
#                                                     </div>
#                                                     <!-- facet options -->
#
#                                                     <div class="phs-facet-results" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-gOyG16">
#                                                         <div ref="facetRef" filtered.bind="searchFacets[facetKey.key] | searchFilter:filterKey:'name'" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-T34Hj9" class="au-target" au-target-id="217">
#                                                             <div class="no-facet-results au-target" aria-live="assertive" aria-atomic="true" data-ph-at-id="no-facet-results" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-LbGIwh" au-target-id="218" data-ph-at-search-keyword-text="">
#                                                                 <!--anchor-->
#
#                                                                 <!--anchor-->
#                                                             </div>
#                                                         </div>
#                                                         <ul data-ph-at-id="facet-results-list" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-ro2kL7">
#                                                             <li data-ph-at-id="facet-results-item" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-eVJPfi">
#                                                                 <label class="phs-checkbox input-check-group" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-I6UzSJ">
#                                                                     <input type="checkbox" model.bind="facet" checked.bind="facet.checked" change.delegate="filterChanged(facet, facetKey.key)" role="checkbox" key-role="lqzfz5-ph-facets-v1-view-external-chkboxRole" data-ph-at-id="facet-checkbox" key-aria-label="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1ChekBoxAriaLabel" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-45xeTf" class="au-target" au-target-id="224" aria-label="Experienced professionals 107 jobs" data-ph-at-text="Experienced professionals" data-ph-at-count="107">
#                                                                     <span class="checkbox" aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-qusfTm">
#                                                                     </span>
#                                                                     <span class="result-text" aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-SaVTMp">Experienced professionals
#                                                                         <span class="result-jobs-count" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-nGOOQq">
#                                                                             <span class="symbol" aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-mDgfey">(</span>107<span class="sym" aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-Sl3WlA">)</span></span><!--anchor--><span class="sr-only" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-TNNA6J"><ppc-content data-ph-at-id="countLabel" key="lqzfz5-ph-facets-v1-view-external-searchFacetsHeadingLevel1JobsPluralText" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-wEGd0L">
#                jobs
#               </ppc-content></span><!--anchor-->
#                                                                     </span>
#                                                                 </label>
#                                                             </li><!--anchor-->
#                                                         </ul>
#                                                     </div>
#                                                 </div><!--anchor-->
#                                             </div>
#                                         </div><div class="panel panel-default refine-widget au-target" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-a1seui" au-target-id="207" data-ph-at-id="facet-country" data-ph-at-text="country">
#                                             <!-- facet heading { bindings :  facetKey }-->
#                                             <div class="panel-heading" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-hoHIq8">
#                                                 <span class="panel-title" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-deX2cm">
#                                                     <button class="facet-menu au-target" keyup.trigger="($event.keyCode === 27)? (facetKey.visible = false):''" click.delegate="adjustAccordian($index)" data-ph-at-id="facet-heading-link" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-uHxChv" au-target-id="208" aria-label="Country/Region" aria-expanded="false" data-ph-at-text="Country/Region">
#                                                         Country/Region
#                                                         <ppc-content type="icon" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-1z3rWp">
#                                                             <i aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-UcYCva" class="au-target icon icon-down-arrow" au-target-id="210"></i>
#                                                         </ppc-content>
#                                                     </button>
#                                                 </span>
#                                             </div>
#                                             <!-- facet options block -->
#                                             <div class="panel-collapse collapse in" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-nvUI3r">
#                                                 <!--anchor-->
#                                             </div>
#                                         </div><div class="panel panel-default refine-widget au-target" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-a1seui" au-target-id="207" data-ph-at-id="facet-state" data-ph-at-text="state">
#                                             <!-- facet heading { bindings :  facetKey }-->
#                                             <div class="panel-heading" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-hoHIq8">
#                                                 <span class="panel-title" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-deX2cm">
#                                                     <button class="facet-menu au-target" keyup.trigger="($event.keyCode === 27)? (facetKey.visible = false):''" click.delegate="adjustAccordian($index)" data-ph-at-id="facet-heading-link" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-uHxChv" au-target-id="208" aria-label="State/Province " aria-expanded="false" data-ph-at-text="State/Province ">
#                                                         State/Province
#                                                         <ppc-content type="icon" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-1z3rWp">
#                                                             <i aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-UcYCva" class="au-target icon icon-down-arrow" au-target-id="210"></i>
#                                                         </ppc-content>
#                                                     </button>
#                                                 </span>
#                                             </div>
#                                             <!-- facet options block -->
#                                             <div class="panel-collapse collapse in" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-nvUI3r">
#                                                 <!--anchor-->
#                                             </div>
#                                         </div><div class="panel panel-default refine-widget au-target" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-a1seui" au-target-id="207" data-ph-at-id="facet-city" data-ph-at-text="city">
#                                             <!-- facet heading { bindings :  facetKey }-->
#                                             <div class="panel-heading" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-hoHIq8">
#                                                 <span class="panel-title" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-deX2cm">
#                                                     <button class="facet-menu au-target" keyup.trigger="($event.keyCode === 27)? (facetKey.visible = false):''" click.delegate="adjustAccordian($index)" data-ph-at-id="facet-heading-link" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-uHxChv" au-target-id="208" aria-label="City" aria-expanded="false" data-ph-at-text="City">
#                                                         City
#                                                         <ppc-content type="icon" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-1z3rWp">
#                                                             <i aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-UcYCva" class="au-target icon icon-down-arrow" au-target-id="210"></i>
#                                                         </ppc-content>
#                                                     </button>
#                                                 </span>
#                                             </div>
#                                             <!-- facet options block -->
#                                             <div class="panel-collapse collapse in" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-nvUI3r">
#                                                 <!--anchor-->
#                                             </div>
#                                         </div><div class="panel panel-default refine-widget au-target" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-a1seui" au-target-id="207" data-ph-at-id="facet-category" data-ph-at-text="category">
#                                             <!-- facet heading { bindings :  facetKey }-->
#                                             <div class="panel-heading" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-hoHIq8">
#                                                 <span class="panel-title" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-deX2cm">
#                                                     <button class="facet-menu au-target" keyup.trigger="($event.keyCode === 27)? (facetKey.visible = false):''" click.delegate="adjustAccordian($index)" data-ph-at-id="facet-heading-link" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-uHxChv" au-target-id="208" aria-label="Profession" aria-expanded="false" data-ph-at-text="Profession">
#                                                         Profession
#                                                         <ppc-content type="icon" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-1z3rWp">
#                                                             <i aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-UcYCva" class="au-target icon icon-down-arrow" au-target-id="210"></i>
#                                                         </ppc-content>
#                                                     </button>
#                                                 </span>
#                                             </div>
#                                             <!-- facet options block -->
#                                             <div class="panel-collapse collapse in" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-nvUI3r">
#                                                 <!--anchor-->
#                                             </div>
#                                         </div><div class="panel panel-default refine-widget au-target" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-a1seui" au-target-id="207" data-ph-at-id="facet-subCategory" data-ph-at-text="subCategory">
#                                             <!-- facet heading { bindings :  facetKey }-->
#                                             <div class="panel-heading" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-hoHIq8">
#                                                 <span class="panel-title" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-deX2cm">
#                                                     <button class="facet-menu au-target" keyup.trigger="($event.keyCode === 27)? (facetKey.visible = false):''" click.delegate="adjustAccordian($index)" data-ph-at-id="facet-heading-link" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-uHxChv" au-target-id="208" aria-label="Discipline" aria-expanded="false" data-ph-at-text="Discipline">
#                                                         Discipline
#                                                         <ppc-content type="icon" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-1z3rWp">
#                                                             <i aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-UcYCva" class="au-target icon icon-down-arrow" au-target-id="210"></i>
#                                                         </ppc-content>
#                                                     </button>
#                                                 </span>
#                                             </div>
#                                             <!-- facet options block -->
#                                             <div class="panel-collapse collapse in" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-nvUI3r">
#                                                 <!--anchor-->
#                                             </div>
#                                         </div><div class="panel panel-default refine-widget au-target" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-a1seui" au-target-id="207" data-ph-at-id="facet-employmentType" data-ph-at-text="employmentType">
#                                             <!-- facet heading { bindings :  facetKey }-->
#                                             <div class="panel-heading" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-hoHIq8">
#                                                 <span class="panel-title" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-deX2cm">
#                                                     <button class="facet-menu au-target" keyup.trigger="($event.keyCode === 27)? (facetKey.visible = false):''" click.delegate="adjustAccordian($index)" data-ph-at-id="facet-heading-link" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-uHxChv" au-target-id="208" aria-label="Employment type " aria-expanded="false" data-ph-at-text="Employment type ">
#                                                         Employment type
#                                                         <ppc-content type="icon" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-1z3rWp">
#                                                             <i aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-UcYCva" class="au-target icon icon-down-arrow" au-target-id="210"></i>
#                                                         </ppc-content>
#                                                     </button>
#                                                 </span>
#                                             </div>
#                                             <!-- facet options block -->
#                                             <div class="panel-collapse collapse in" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-nvUI3r">
#                                                 <!--anchor-->
#                                             </div>
#                                         </div><div class="panel panel-default refine-widget au-target" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-a1seui" au-target-id="207" data-ph-at-id="facet-requisitionRoleType" data-ph-at-text="requisitionRoleType">
#                                             <!-- facet heading { bindings :  facetKey }-->
#                                             <div class="panel-heading" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-hoHIq8">
#                                                 <span class="panel-title" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-deX2cm">
#                                                     <button class="facet-menu au-target" keyup.trigger="($event.keyCode === 27)? (facetKey.visible = false):''" click.delegate="adjustAccordian($index)" data-ph-at-id="facet-heading-link" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-uHxChv" au-target-id="208" aria-label="Role type" aria-expanded="false" data-ph-at-text="Role type">
#                                                         Role type
#                                                         <ppc-content type="icon" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-1z3rWp">
#                                                             <i aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-UcYCva" class="au-target icon icon-down-arrow" au-target-id="210"></i>
#                                                         </ppc-content>
#                                                     </button>
#                                                 </span>
#                                             </div>
#                                             <!-- facet options block -->
#                                             <div class="panel-collapse collapse in" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-nvUI3r">
#                                                 <!--anchor-->
#                                             </div>
#                                         </div><div class="panel panel-default refine-widget au-target" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-a1seui" au-target-id="207" data-ph-at-id="facet-educationLevel" data-ph-at-text="educationLevel">
#                                             <!-- facet heading { bindings :  facetKey }-->
#                                             <div class="panel-heading" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-hoHIq8">
#                                                 <span class="panel-title" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-deX2cm">
#                                                     <button class="facet-menu au-target" keyup.trigger="($event.keyCode === 27)? (facetKey.visible = false):''" click.delegate="adjustAccordian($index)" data-ph-at-id="facet-heading-link" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-uHxChv" au-target-id="208" aria-label="Level of education" aria-expanded="false" data-ph-at-text="Level of education">
#                                                         Level of education
#                                                         <ppc-content type="icon" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-1z3rWp">
#                                                             <i aria-hidden="true" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-UcYCva" class="au-target icon icon-down-arrow" au-target-id="210"></i>
#                                                         </ppc-content>
#                                                     </button>
#                                                 </span>
#                                             </div>
#                                             <!-- facet options block -->
#                                             <div class="panel-collapse collapse in" data-ph-id="ph-view-external-1566490250358-ph-facets-v1lqzfz5-nvUI3r">
#                                                 <!--anchor-->
#                                             </div>
#                                         </div><!--anchor-->
#                                     </div>
#                                     <!-- <div class="phs-bottom-hide-filter">
#                                         <a href="javascript:void(0)" click.delegate="handleDoneButtonClick()" class="btn primary-button btn-block" aria-label="Refine Search" key-aria-label="refineSearchBtnLabel" role="button" key-role="btnRole" data-ph-at-id="mobile-facet-filter-done-button">
#                                             <ppc-content key="refineSearch" data-ph-at-id="mobile-facet-filter-done-button">
#                                                 Refine Search
#                                             </ppc-content>
#                                         </a>
#                                     </div> -->
#                                 </div>
#                                 <!-- static text for internal -->
#                                 <!-- <div class="hiring-content-block" if.bind="commonService.getSiteType() == 'internal'">
#                                     <div class="hiring-main-block">
#                                         <h2>
#                                             <ppc-content key="searchFacetsHeadingLevel2InternalJobsSearchText">Internal job search</ppc-content>
#                                         </h2>
#                                         <p>
#                                             <ppc-content key="searchFacetsHeadingLevel2InternalJobsSearchDescText">Looking for a job posted under a specific hiring manager? Enter their alias in the search bar at the top or in the keyword search and any jobs listing them as the hiring manager will be displayed. </ppc-content>
#                                         </p>
#                                     </div>
#                                 </div> -->
#                             <!--anchor--></div>
#        </section>
#        <!--End Search Facets block -->
#        <!-- Create job alert block -->
#        <section class="ph-widget" instance-id="46yred" view="46yred-default" original-view="default" data-ph-id="ph-page-element-page19-IF0bUG">
#         <div as-element="ph-create-job-alert-v1" data-widget="ph-create-job-alert-v1" class="ph-create-job-alert-v1-default-default ph-widget-target au-target" instance-id="46yred" view="46yred-default" original-view="default" data-ph-id="ph-page-element-page19-ZDI2Dk" au-target-id="34">
#
#    <!--anchor--> <!--anchor--></div>
#        </section>
#        <!--End Create job alert block -->
#       </div>
#       <!-- End Left side block-->
#       <!-- Right side block -->
#       <div class="col-md-8 col-sm-7" data-ph-id="ph-page-element-page19-4KBXNX">
#        <!-- Search Results block-->
#        <section class="ph-widget" instance-id="2fssdu" view="2fssdu-view-external" original-view="view-external" data-ph-id="ph-page-element-page19-7hjyCS">
#         <div as-element="ph-search-results-v1" bulkcart.bind="true" data-widget="ph-search-results-v1" class="ph-search-results-v1-view-external-default ph-widget-target au-target" view="view-external-1565777110191" is-error-msg-reqd.bind="true" instance-id="2fssdu" original-view="view-external" data-ph-id="ph-page-element-page19-o7gVzj" au-target-id="35">
#
#
#                                 <!-- <span class="sr-only" aria-live="assertive" aria-hidden="true" aria-atomic="true" innerhtml="${isDataUpdated ? 'Showing '+startingJobNumberInPage+' to '+endingJobNumberInpage+ ' of '+ totalJobs + createdAlertName +' jobs' : ''}"></span> -->
#
#                                 <div class="phs-facet-results-block" role="region" aria-label="Search results block" key-aria-label="2fssdu-ph-search-results-v1-view-external-srRegionBlockAriaLabelText" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-2gJFYk">
#                                     <div class="show-loader au-target aurelia-hide" ph-loading-img="show-loader.bind: showLoader" show.bind="showLoader" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-E6fPuu" au-target-id="256"></div>
#                                     <div class="phs-results-actions" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-E4WXyi">
#                                         <!--Header part for search results-->
#                                         <div class="phs-jobs-list-header row au-target" data-ph-at-id="jobs-list-header" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-YOneBz" au-target-id="257" data-ph-at-search-keyword-text="php">
#                                             <!-- Result count block -->
#                                             <div id="content" aria-live="assertive" aria-atomic="true" class="col-xs-8 au-target" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-nki5yM" au-target-id="258" data-ph-at-starting-job-number-text="1" data-ph-at-ending-job-number-text="20" data-ph-at-total-jobs-text="107">
#                                                 <div data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-6B1ulD">
#                                                     <span data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Z8kD3k">
#                                                         <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultText" data-ph-at-id="showing-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5ou0Pc">
#           Showing
#         </ppc-content>
#                                                         <span class="job-number" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-RdIQRR"> 1 </span>
#                                                         <span class="job-number" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-I5vvvg">
#                                                             <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultHyphenText" data-ph-at-id="hyphen-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-T2wITv">
#            -
#          </ppc-content>
#                                                         </span>
#                                                         <span class="sr-only" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Hw2vPe"><ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultToText" data-ph-at-id="to-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-UPlP8x">
#           to
#          </ppc-content></span>
#                                                         <span class="job-number" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-p6nkOz"> 20 </span>
#                                                         <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultOfText" data-ph-at-id="of-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-iQfvpC">
#           of
#         </ppc-content>
#                                                     </span><!--anchor-->
#                                                     <span class="total-jobs" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-m0Utvg"> 107 </span>
#                                                     <!--anchor-->
#                                                     <span data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-9b58l8">
#                                                         <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultResText" data-ph-at-id="results-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-uYhx5J">
#          results
#         </ppc-content>
#                                                     </span><!--anchor-->
#                                                     <span data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Z9NTA6">
#                                                         <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultForText" data-ph-at-id="for-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-O8Z3mV">
#          for
#         </ppc-content>
#                                                     </span><!--anchor-->
#                                                     <span class="search-keyword" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-trD4PI">php</span><!--anchor-->
#                                                     <!--anchor-->
#                                                 </div><!--anchor-->
#                                             </div>
#                                             <!--End Result count block -->
#                                             <div class="col-xs-4" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-1bVDI4">
#                                                 <div class="remove-padding" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Wia4kL">
#                                                     <div class="pull-right phs-header-controls" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Y89J9E">
#                                                         <!-- Filter block hidden mode-->
#                                                         <div tabindex="0" class="phs-jobs-list-count au-target" show.bind="totalJobs > 0" data-ph-at-id="search-page-top-job-count" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-hrbnzX" au-target-id="271" aria-label="107 jobs" data-ph-at-count="107">
#                                                             107
#                                                             <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultForJobsPluralText" data-ph-at-id="countLabel" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CyOWBa">
#            jobs
#           </ppc-content>
#                                                         </div>
#                                                         <div class="phs-filter" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-WHQsVH">
#                                                             <a href="javascript:void(0)" click.delegate="showFacetFilter()" aria-label="Filter button" key-aria-label="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultFilterAriaLabelText" data-ph-at-id="mobile-facet-filter-menu-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-WNeBYS" class="au-target" au-target-id="273">
#                                                                 <ppc-content type="icon" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-efY17s">
#                                                                     <i class="icon icon-filter" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-aEWA2L"></i>
#                                                                 </ppc-content>
#                                                             </a>
#                                                         </div>
#                                                         <!--End Filter block -->
#
#                                                         <!-- sort jobs block -->
#                                                         <div class="phs-jobs-list-sort phs-taglib" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-clNZVf">
#                                                             <label for="sortselect" class="control-label" data-ph-at-id="sortby-label" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-raRQki">
#                                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSortJobsText" data-ph-at-id="sortby-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-8v2Zsx">
#             Sort by
#            </ppc-content>
#                                                             </label>
#                                                             <div class="sortby" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-pFhfla">
#                                                                 <select id="sortselect" aria-label="Sort by" key-aria-label="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSortJobsAriaLabelText" class="form-control au-target" value.bind="searchParams.sortBy" change.delegate="sortfilterSearch($event)" data-ph-at-id="sortby-drop-down" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-mxiPkX" au-target-id="274">
#                                                                     <option value="Most relevant" key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSortJobsOptions1" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-P5ywOC">Most relevant</option>
#                                                                     <option value="Most recent" key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSortJobsOptions2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-dg5AHq">Most recent</option>
#                                                                     <option value="Most popular" key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSortJobsOptions3" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-PhOKut">Most popular</option><!--anchor-->
#                                                                 </select>
#                                                                 <i class="icon icon-down-arrow" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ccUqwU"></i>
#                                                             </div>
#                                                         </div>
#                                                          <!--End sort jobs block -->
#                                                     </div>
#                                                 </div><!--anchor-->
#                                             </div>
#                                         </div>
#                                         <!--End Header part for search results-->
#
#                                         <!--Selected Facet Tags-->
#                                         <!--anchor-->
#                                         <!--End Seleceted Facet Tags-->
#                                     </div>
#                                     <div show.bind="!showLoader &amp;&amp; totalJobs" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-hI3iJF" class="au-target" au-target-id="286">
#                                         <!--Facet results-->
#                                         <div class="phs-jobs-list" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-1E6CFC">
#                                             <div class="phs-jobs-block" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-xd06Qs">
#                                                 <ul data-ph-at-id="jobs-list" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-a2DVXy" class="au-target" au-target-id="287" data-ph-at-widget-data-count="20">
#                                                     <li class="jobs-list-item" data-ph-at-id="jobs-list-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-y4hTr0">
#                                                         <div class="information-block row" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-zEw2pE">
#                                                             <div class="left-block col-xs-12 col-md-10" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-rmeHWW">
#                                                                 <!-- jobs link block -->
#                                                                 <div class="information" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-fm9Dgs">
#                                                                     <a focus.bind="$index == 0 &amp;&amp; currentSelectedPage > 1" ph-tevent="job_click" ref="linkEle" role="link" key-role="2fssdu-ph-search-results-v1-view-external-linkRole" target="_blank" data-ph-at-id="job-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ic7VNu" class="au-target" au-target-id="288" ph-click-ctx="job" ph-tref="15696698684291aa88" ph-tag="ph-search-results-v1" href="https://careers.microsoft.com/us/en/job/568231/Senior-Business-Manager" aria-label="Senior Business Manager job ID 568231 opens in a new tab" data-ph-at-job-title-text="Senior Business Manager" data-ph-at-job-location-text="Redmond, Washington, United States" data-ph-at-job-category-text="Business Programs &amp; Operations" data-ph-at-job-id-text="568231" data-ph-at-job-type-text="" data-ph-at-job-industry-text="" data-ph-at-job-post-date-text="2019-01-04T01:22:00" data-ph-at-job-seqno-text="568231" data-ph-at-job-position-text="" data-ph-at-job-employment-type-text="" data-ph-at-job-role-type-text="" data-ph-at-job-education-level-text="">
#                                                                         <span class="job-title" data-ph-at-id="searchresults-job-title" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-MRnq6A">Senior Business Manager</span>
#                                                                     </a>
#                                                                     <div class="job-additional-info" data-ph-at-id="job-info" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LesJKv">
#                                                                         <span class="job-location" data-ph-at-id="searchresults-job-location" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CQMOUl">
#                                                                             Redmond, Washington, United States
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-category" data-ph-at-id="searchresults-job-category" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-g94YTa">
#                                                                             Business Programs &amp; Operations
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-date au-target" data-ph-at-id="searchresults-job-postdate" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-b6UGw3" au-target-id="294" aria-label="Jan 4th 2019">
#                                                                             Jan 4, 2019
#                                                                         </span><!--anchor-->
#                                                                     </div>
#                                                                     <div class="description au-target" innerhtml.bind="eachResult.descriptionTeaser | sanitizeHTML" data-ph-at-id="jobdescription-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Abw08f" au-target-id="297">Developer Division works at the center of Microsoft strategic initiatives – building the tools and services other developers use to build software for Azure, Xbox, Windows, Mac OS, iOS, Android,</div>
#                                                                 </div>
#                                                                 <!--End jobs link block -->
#
#                                                                 <!-- jobs multilocation block -->
#                                                                 <!--anchor-->
#                                                                 <!--End jobs multilocation block -->
#                                                             </div>
#                                                             <div class="right-block col-xs-12 col-md-2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-W9vvx1">
#                                                                 <!-- Job applied status block -->
#                                                                 <div class="applied-action" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0WA3mP">
#                                                                     <section class="ph-widget" instance-id="we3alx" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CGkAfP" view="1565777110184-default" original-view="default" theme="default">
#                                                                         <div as-element="ph-job-status-v1" arrjoblist.bind="$index===0 ? jobResults : null" jobid="${eachResult.jobSeqNo}" view="1565777110184-default" mode="APPLY" class="ph-job-status-v1-default-default ph-widget-target au-target" data-widget="ph-job-status-v1" instance-id="we3alx" original-view="default" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TWsAYD" au-target-id="306">
#
#                                                                             <!--anchor-->
#                                                                         <!--anchor--></div>
#                                                                     </section>
#                                                                 </div>
#                                                                 <!--End Job applied status block -->
#
#                                                                 <!-- Job saved block -->
#                                                                 <div class="actions" data-ph-at-id="job-actions" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Kt42DX">
#                                                                     <!--<div as-element="ph-add-to-cart-v1" if.bind="!bulkcart" data-widget="ph-add-to-cart-v1" job-detail.bind="eachResult" class="ph-add-to-cart-v1-default-default" view="view1"></div>-->
#                                                                     <div class="savejob-checkbox" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-lWmxkg">
#                                                                         <label data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-eySiqX" class="au-target" au-target-id="307" for="save-568231-0">
#                                                                             <input type="checkbox" checked.bind="eachResult.isJobSaved" change.delegate="handleSaveJob(eachResult)" role="checkbox" data-ph-at-id="save-click" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LoOray" class="au-target" au-target-id="308" id="save-568231-0" aria-label="Save Senior Business Manager job ID 568231 to job cart" aria-checked="false">
#                                                                             <span class="label-content" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5iZTnr">
#                                                                                 <i class="icon icon-star-empty" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-3hSiPg"></i>
#                                                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSaveText" data-ph-at-id="save-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-V3uiSa">
#                 Save
#                </ppc-content>
#                                                                             </span><!--anchor-->
#                                                                             <!--anchor-->
#                                                                         </label>
#                                                                     </div><!--anchor-->
#                                                                 </div>
#                                                                  <!--End Job saved block -->
#                                                             </div>
#                                                         </div>
#                                                     </li><li class="jobs-list-item" data-ph-at-id="jobs-list-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-y4hTr0">
#                                                         <div class="information-block row" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-zEw2pE">
#                                                             <div class="left-block col-xs-12 col-md-10" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-rmeHWW">
#                                                                 <!-- jobs link block -->
#                                                                 <div class="information" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-fm9Dgs">
#                                                                     <a focus.bind="$index == 0 &amp;&amp; currentSelectedPage > 1" ph-tevent="job_click" ref="linkEle" role="link" key-role="2fssdu-ph-search-results-v1-view-external-linkRole" target="_blank" data-ph-at-id="job-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ic7VNu" class="au-target" au-target-id="288" ph-click-ctx="job" ph-tref="156966986843015e94" ph-tag="ph-search-results-v1" href="https://careers.microsoft.com/us/en/job/668332/Support-Escalation-Engineer" aria-label="Support Escalation Engineer job ID 668332 opens in a new tab" data-ph-at-job-title-text="Support Escalation Engineer" data-ph-at-job-location-text="Bangalore, Karnataka, India" data-ph-at-job-category-text="Services" data-ph-at-job-id-text="668332" data-ph-at-job-type-text="" data-ph-at-job-industry-text="" data-ph-at-job-post-date-text="2019-07-15T06:15:00" data-ph-at-job-seqno-text="668332" data-ph-at-job-position-text="" data-ph-at-job-employment-type-text="" data-ph-at-job-role-type-text="" data-ph-at-job-education-level-text="">
#                                                                         <span class="job-title" data-ph-at-id="searchresults-job-title" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-MRnq6A">Support Escalation Engineer</span>
#                                                                     </a>
#                                                                     <div class="job-additional-info" data-ph-at-id="job-info" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LesJKv">
#                                                                         <span class="job-location" data-ph-at-id="searchresults-job-location" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CQMOUl">
#                                                                             Bangalore, Karnataka, India
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-category" data-ph-at-id="searchresults-job-category" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-g94YTa">
#                                                                             Services
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-date au-target" data-ph-at-id="searchresults-job-postdate" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-b6UGw3" au-target-id="294" aria-label="Jul 15th 2019">
#                                                                             Jul 15, 2019
#                                                                         </span><!--anchor-->
#                                                                     </div>
#                                                                     <div class="description au-target" innerhtml.bind="eachResult.descriptionTeaser | sanitizeHTML" data-ph-at-id="jobdescription-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Abw08f" au-target-id="297">Job DescriptionTo provide information and responsive and reliable resolution of the most critical and highest impact problems for Microsoft’s strategic corporate customers using Azure App</div>
#                                                                 </div>
#                                                                 <!--End jobs link block -->
#
#                                                                 <!-- jobs multilocation block -->
#                                                                 <!--anchor-->
#                                                                 <!--End jobs multilocation block -->
#                                                             </div>
#                                                             <div class="right-block col-xs-12 col-md-2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-W9vvx1">
#                                                                 <!-- Job applied status block -->
#                                                                 <div class="applied-action" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0WA3mP">
#                                                                     <section class="ph-widget" instance-id="we3alx" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CGkAfP" view="1565777110184-default" original-view="default" theme="default">
#                                                                         <div as-element="ph-job-status-v1" arrjoblist.bind="$index===0 ? jobResults : null" jobid="${eachResult.jobSeqNo}" view="1565777110184-default" mode="APPLY" class="ph-job-status-v1-default-default ph-widget-target au-target" data-widget="ph-job-status-v1" instance-id="we3alx" original-view="default" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TWsAYD" au-target-id="306">
#
#                                                                             <!--anchor-->
#                                                                         <!--anchor--></div>
#                                                                     </section>
#                                                                 </div>
#                                                                 <!--End Job applied status block -->
#
#                                                                 <!-- Job saved block -->
#                                                                 <div class="actions" data-ph-at-id="job-actions" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Kt42DX">
#                                                                     <!--<div as-element="ph-add-to-cart-v1" if.bind="!bulkcart" data-widget="ph-add-to-cart-v1" job-detail.bind="eachResult" class="ph-add-to-cart-v1-default-default" view="view1"></div>-->
#                                                                     <div class="savejob-checkbox" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-lWmxkg">
#                                                                         <label data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-eySiqX" class="au-target" au-target-id="307" for="save-668332-1">
#                                                                             <input type="checkbox" checked.bind="eachResult.isJobSaved" change.delegate="handleSaveJob(eachResult)" role="checkbox" data-ph-at-id="save-click" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LoOray" class="au-target" au-target-id="308" id="save-668332-1" aria-label="Save Support Escalation Engineer job ID 668332 to job cart" aria-checked="false">
#                                                                             <span class="label-content" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5iZTnr">
#                                                                                 <i class="icon icon-star-empty" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-3hSiPg"></i>
#                                                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSaveText" data-ph-at-id="save-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-V3uiSa">
#                 Save
#                </ppc-content>
#                                                                             </span><!--anchor-->
#                                                                             <!--anchor-->
#                                                                         </label>
#                                                                     </div><!--anchor-->
#                                                                 </div>
#                                                                  <!--End Job saved block -->
#                                                             </div>
#                                                         </div>
#                                                     </li><li class="jobs-list-item" data-ph-at-id="jobs-list-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-y4hTr0">
#                                                         <div class="information-block row" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-zEw2pE">
#                                                             <div class="left-block col-xs-12 col-md-10" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-rmeHWW">
#                                                                 <!-- jobs link block -->
#                                                                 <div class="information" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-fm9Dgs">
#                                                                     <a focus.bind="$index == 0 &amp;&amp; currentSelectedPage > 1" ph-tevent="job_click" ref="linkEle" role="link" key-role="2fssdu-ph-search-results-v1-view-external-linkRole" target="_blank" data-ph-at-id="job-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ic7VNu" class="au-target" au-target-id="288" ph-click-ctx="job" ph-tref="156966986843111fb0" ph-tag="ph-search-results-v1" href="https://careers.microsoft.com/us/en/job/708695/Program-Manager" aria-label="Program Manager job ID 708695 opens in a new tab" data-ph-at-job-title-text="Program Manager" data-ph-at-job-location-text="Redmond, Washington, United States" data-ph-at-job-category-text="Engineering" data-ph-at-job-id-text="708695" data-ph-at-job-type-text="" data-ph-at-job-industry-text="" data-ph-at-job-post-date-text="2019-09-20T18:34:00" data-ph-at-job-seqno-text="708695" data-ph-at-job-position-text="" data-ph-at-job-employment-type-text="" data-ph-at-job-role-type-text="" data-ph-at-job-education-level-text="">
#                                                                         <span class="job-title" data-ph-at-id="searchresults-job-title" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-MRnq6A">Program Manager</span>
#                                                                     </a>
#                                                                     <div class="job-additional-info" data-ph-at-id="job-info" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LesJKv">
#                                                                         <span class="job-location" data-ph-at-id="searchresults-job-location" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CQMOUl">
#                                                                             Redmond, Washington, United States
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-category" data-ph-at-id="searchresults-job-category" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-g94YTa">
#                                                                             Engineering
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-date au-target" data-ph-at-id="searchresults-job-postdate" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-b6UGw3" au-target-id="294" aria-label="Sep 20th 2019">
#                                                                             Sep 20, 2019
#                                                                         </span><!--anchor-->
#                                                                     </div>
#                                                                     <div class="description au-target" innerhtml.bind="eachResult.descriptionTeaser | sanitizeHTML" data-ph-at-id="jobdescription-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Abw08f" au-target-id="297">LEAP Program Candidates - Are you ready for the opportunity to make a billion people more productive with software? Do you have the right skills to write and maintain services? We are looking for</div>
#                                                                 </div>
#                                                                 <!--End jobs link block -->
#
#                                                                 <!-- jobs multilocation block -->
#                                                                 <!--anchor-->
#                                                                 <!--End jobs multilocation block -->
#                                                             </div>
#                                                             <div class="right-block col-xs-12 col-md-2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-W9vvx1">
#                                                                 <!-- Job applied status block -->
#                                                                 <div class="applied-action" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0WA3mP">
#                                                                     <section class="ph-widget" instance-id="we3alx" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CGkAfP" view="1565777110184-default" original-view="default" theme="default">
#                                                                         <div as-element="ph-job-status-v1" arrjoblist.bind="$index===0 ? jobResults : null" jobid="${eachResult.jobSeqNo}" view="1565777110184-default" mode="APPLY" class="ph-job-status-v1-default-default ph-widget-target au-target" data-widget="ph-job-status-v1" instance-id="we3alx" original-view="default" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TWsAYD" au-target-id="306">
#
#                                                                             <!--anchor-->
#                                                                         <!--anchor--></div>
#                                                                     </section>
#                                                                 </div>
#                                                                 <!--End Job applied status block -->
#
#                                                                 <!-- Job saved block -->
#                                                                 <div class="actions" data-ph-at-id="job-actions" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Kt42DX">
#                                                                     <!--<div as-element="ph-add-to-cart-v1" if.bind="!bulkcart" data-widget="ph-add-to-cart-v1" job-detail.bind="eachResult" class="ph-add-to-cart-v1-default-default" view="view1"></div>-->
#                                                                     <div class="savejob-checkbox" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-lWmxkg">
#                                                                         <label data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-eySiqX" class="au-target" au-target-id="307" for="save-708695-2">
#                                                                             <input type="checkbox" checked.bind="eachResult.isJobSaved" change.delegate="handleSaveJob(eachResult)" role="checkbox" data-ph-at-id="save-click" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LoOray" class="au-target" au-target-id="308" id="save-708695-2" aria-label="Save Program Manager job ID 708695 to job cart" aria-checked="false">
#                                                                             <span class="label-content" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5iZTnr">
#                                                                                 <i class="icon icon-star-empty" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-3hSiPg"></i>
#                                                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSaveText" data-ph-at-id="save-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-V3uiSa">
#                 Save
#                </ppc-content>
#                                                                             </span><!--anchor-->
#                                                                             <!--anchor-->
#                                                                         </label>
#                                                                     </div><!--anchor-->
#                                                                 </div>
#                                                                  <!--End Job saved block -->
#                                                             </div>
#                                                         </div>
#                                                     </li><li class="jobs-list-item" data-ph-at-id="jobs-list-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-y4hTr0">
#                                                         <div class="information-block row" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-zEw2pE">
#                                                             <div class="left-block col-xs-12 col-md-10" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-rmeHWW">
#                                                                 <!-- jobs link block -->
#                                                                 <div class="information" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-fm9Dgs">
#                                                                     <a focus.bind="$index == 0 &amp;&amp; currentSelectedPage > 1" ph-tevent="job_click" ref="linkEle" role="link" key-role="2fssdu-ph-search-results-v1-view-external-linkRole" target="_blank" data-ph-at-id="job-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ic7VNu" class="au-target" au-target-id="288" ph-click-ctx="job" ph-tref="156966986843115001" ph-tag="ph-search-results-v1" href="https://careers.microsoft.com/us/en/job/700085/Azure-Database-for-PostgreSQL-MySQL-MariaDB-Dev-Support-Engineer" aria-label="Azure Database for PostgreSQL/MySQL/MariaDB Dev Support Engineer job ID 700085 opens in a new tab" data-ph-at-job-title-text="Azure Database for PostgreSQL/MySQL/MariaDB Dev Support Engineer" data-ph-at-job-location-text="Bucharest, Bucharest, Romania" data-ph-at-job-category-text="Services" data-ph-at-job-id-text="700085" data-ph-at-job-type-text="" data-ph-at-job-industry-text="" data-ph-at-job-post-date-text="2019-09-12T10:18:00" data-ph-at-job-seqno-text="700085" data-ph-at-job-position-text="" data-ph-at-job-employment-type-text="" data-ph-at-job-role-type-text="" data-ph-at-job-education-level-text="">
#                                                                         <span class="job-title" data-ph-at-id="searchresults-job-title" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-MRnq6A">Azure Database for PostgreSQL/MySQL/MariaDB Dev Support Engineer</span>
#                                                                     </a>
#                                                                     <div class="job-additional-info" data-ph-at-id="job-info" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LesJKv">
#                                                                         <!--anchor-->
#                                                                         <span class="job-category" data-ph-at-id="searchresults-job-category" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-g94YTa">
#                                                                             Services
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-date au-target" data-ph-at-id="searchresults-job-postdate" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-b6UGw3" au-target-id="294" aria-label="Sep 12th 2019">
#                                                                             Sep 12, 2019
#                                                                         </span><!--anchor-->
#                                                                     </div>
#                                                                     <div class="description au-target" innerhtml.bind="eachResult.descriptionTeaser | sanitizeHTML" data-ph-at-id="jobdescription-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Abw08f" au-target-id="297">Role overview:Azure Database for PostgreSQL and MySQL support is a becoming a strategic unit of MicrosoftCustomer Support Services (CSS). As a Support Engineer, you will represent Microsoft in</div>
#                                                                 </div>
#                                                                 <!--End jobs link block -->
#
#                                                                 <!-- jobs multilocation block -->
#                                                                 <div class="job-multi-locations" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-vJOVzG">
#                                                                     <button ph-tevent="multi_location_click" keyup.trigger="($event.keyCode === 27)?(eachResult.toggleOpen = false):''" class="esc$$close au-target" click.delegate="eachResult.toggleOpen = !eachResult.toggleOpen" role="button" key-role="IWwth6-2fssdu-ph-search-results-v1-view-external-btnRole" data-ph-at-id="job-multi-locations-button" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0aUp1e" au-target-id="298" data-ph-tevent-attr-trait14="Services" data-ph-tevent-attr-trait5="700085" id="searchLoc-3" aria-expanded="false" aria-label="Azure Database for PostgreSQL/MySQL/MariaDB Dev Support Engineer job ID 700085 Job available in 3 locations" data-ph-at-job-multilocation-count="3">
#                                                                         <span data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-h6pjaT"><ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultJobAvailText1" data-ph-at-id="multilocation-text1" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5DjjWH">
#               Job available in
#              </ppc-content></span> 3 <span data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5Lm1HA"><ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultJobAvailText2" data-ph-at-id="multilocation-text2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-2Go8OT">
#               locations
#              </ppc-content></span>
#                                                                         <!--icon toggle based on item click: js dependent-->
#                                                                         <!--<i ref="listItemIcon" class="icon icon-down-arrow" aria-hidden="true"></i>-->
#                                                                         <i ref="listItemIcon" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-KotPHt" class="au-target icon icon-down-arrow" au-target-id="300"></i>
#                                                                     </button>
#                                                                     <!--dropView used to toggle toggleMultiLocationView based on item click: js dependent-->
#                                                                     <ul ref="listItem" data-ph-at-id="job-multi-locations-list" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-cbms8u" class="au-target hide" au-target-id="301" aria-hidden="true">
#                                                                         <li class="location au-target" data-ph-at-id="job-multi-location-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-EgsS0Q" au-target-id="302" aria-label="Bucharest, Bucharest, Romania" data-ph-at-job-location-text="Bucharest, Bucharest, Romania">
#                                                                             Bucharest, Bucharest, Romania
#                                                                         </li><li class="location au-target" data-ph-at-id="job-multi-location-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-EgsS0Q" au-target-id="302" aria-label="Other, Other, Portugal" data-ph-at-job-location-text="Other, Other, Portugal">
#                                                                             Other, Other, Portugal
#                                                                         </li><li class="location au-target" data-ph-at-id="job-multi-location-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-EgsS0Q" au-target-id="302" aria-label="Other, Other, Jordan" data-ph-at-job-location-text="Other, Other, Jordan">
#                                                                             Other, Other, Jordan
#                                                                         </li><!--anchor-->
#                                                                     </ul>
#                                                                 </div><!--anchor-->
#                                                                 <!--End jobs multilocation block -->
#                                                             </div>
#                                                             <div class="right-block col-xs-12 col-md-2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-W9vvx1">
#                                                                 <!-- Job applied status block -->
#                                                                 <div class="applied-action" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0WA3mP">
#                                                                     <section class="ph-widget" instance-id="we3alx" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CGkAfP" view="1565777110184-default" original-view="default" theme="default">
#                                                                         <div as-element="ph-job-status-v1" arrjoblist.bind="$index===0 ? jobResults : null" jobid="${eachResult.jobSeqNo}" view="1565777110184-default" mode="APPLY" class="ph-job-status-v1-default-default ph-widget-target au-target" data-widget="ph-job-status-v1" instance-id="we3alx" original-view="default" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TWsAYD" au-target-id="306">
#
#                                                                             <!--anchor-->
#                                                                         <!--anchor--></div>
#                                                                     </section>
#                                                                 </div>
#                                                                 <!--End Job applied status block -->
#
#                                                                 <!-- Job saved block -->
#                                                                 <div class="actions" data-ph-at-id="job-actions" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Kt42DX">
#                                                                     <!--<div as-element="ph-add-to-cart-v1" if.bind="!bulkcart" data-widget="ph-add-to-cart-v1" job-detail.bind="eachResult" class="ph-add-to-cart-v1-default-default" view="view1"></div>-->
#                                                                     <div class="savejob-checkbox" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-lWmxkg">
#                                                                         <label data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-eySiqX" class="au-target" au-target-id="307" for="save-700085-3">
#                                                                             <input type="checkbox" checked.bind="eachResult.isJobSaved" change.delegate="handleSaveJob(eachResult)" role="checkbox" data-ph-at-id="save-click" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LoOray" class="au-target" au-target-id="308" id="save-700085-3" aria-label="Save Azure Database for PostgreSQL/MySQL/MariaDB Dev Support Engineer job ID 700085 to job cart" aria-checked="false">
#                                                                             <span class="label-content" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5iZTnr">
#                                                                                 <i class="icon icon-star-empty" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-3hSiPg"></i>
#                                                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSaveText" data-ph-at-id="save-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-V3uiSa">
#                 Save
#                </ppc-content>
#                                                                             </span><!--anchor-->
#                                                                             <!--anchor-->
#                                                                         </label>
#                                                                     </div><!--anchor-->
#                                                                 </div>
#                                                                  <!--End Job saved block -->
#                                                             </div>
#                                                         </div>
#                                                     </li><li class="jobs-list-item" data-ph-at-id="jobs-list-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-y4hTr0">
#                                                         <div class="information-block row" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-zEw2pE">
#                                                             <div class="left-block col-xs-12 col-md-10" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-rmeHWW">
#                                                                 <!-- jobs link block -->
#                                                                 <div class="information" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-fm9Dgs">
#                                                                     <a focus.bind="$index == 0 &amp;&amp; currentSelectedPage > 1" ph-tevent="job_click" ref="linkEle" role="link" key-role="2fssdu-ph-search-results-v1-view-external-linkRole" target="_blank" data-ph-at-id="job-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ic7VNu" class="au-target" au-target-id="288" ph-click-ctx="job" ph-tref="15696698684321904e" ph-tag="ph-search-results-v1" href="https://careers.microsoft.com/us/en/job/625478/Support-Engineer" aria-label="Support Engineer job ID 625478 opens in a new tab" data-ph-at-job-title-text="Support Engineer" data-ph-at-job-location-text="Bangalore, Karnataka, India" data-ph-at-job-category-text="Services" data-ph-at-job-id-text="625478" data-ph-at-job-type-text="" data-ph-at-job-industry-text="" data-ph-at-job-post-date-text="2019-06-30T09:10:00" data-ph-at-job-seqno-text="625478" data-ph-at-job-position-text="" data-ph-at-job-employment-type-text="" data-ph-at-job-role-type-text="" data-ph-at-job-education-level-text="">
#                                                                         <span class="job-title" data-ph-at-id="searchresults-job-title" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-MRnq6A">Support Engineer</span>
#                                                                     </a>
#                                                                     <div class="job-additional-info" data-ph-at-id="job-info" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LesJKv">
#                                                                         <span class="job-location" data-ph-at-id="searchresults-job-location" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CQMOUl">
#                                                                             Bangalore, Karnataka, India
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-category" data-ph-at-id="searchresults-job-category" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-g94YTa">
#                                                                             Services
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-date au-target" data-ph-at-id="searchresults-job-postdate" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-b6UGw3" au-target-id="294" aria-label="Jun 30th 2019">
#                                                                             Jun 30, 2019
#                                                                         </span><!--anchor-->
#                                                                     </div>
#                                                                     <div class="description au-target" innerhtml.bind="eachResult.descriptionTeaser | sanitizeHTML" data-ph-at-id="jobdescription-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Abw08f" au-target-id="297">Azure Database for PostgreSQL and MySQL Support Engineer Role overview: Azure Database for PostgreSQL and MySQL support is a becoming a strategic unit of Microsoft Customer Support Services (CSS). As</div>
#                                                                 </div>
#                                                                 <!--End jobs link block -->
#
#                                                                 <!-- jobs multilocation block -->
#                                                                 <!--anchor-->
#                                                                 <!--End jobs multilocation block -->
#                                                             </div>
#                                                             <div class="right-block col-xs-12 col-md-2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-W9vvx1">
#                                                                 <!-- Job applied status block -->
#                                                                 <div class="applied-action" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0WA3mP">
#                                                                     <section class="ph-widget" instance-id="we3alx" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CGkAfP" view="1565777110184-default" original-view="default" theme="default">
#                                                                         <div as-element="ph-job-status-v1" arrjoblist.bind="$index===0 ? jobResults : null" jobid="${eachResult.jobSeqNo}" view="1565777110184-default" mode="APPLY" class="ph-job-status-v1-default-default ph-widget-target au-target" data-widget="ph-job-status-v1" instance-id="we3alx" original-view="default" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TWsAYD" au-target-id="306">
#
#                                                                             <!--anchor-->
#                                                                         <!--anchor--></div>
#                                                                     </section>
#                                                                 </div>
#                                                                 <!--End Job applied status block -->
#
#                                                                 <!-- Job saved block -->
#                                                                 <div class="actions" data-ph-at-id="job-actions" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Kt42DX">
#                                                                     <!--<div as-element="ph-add-to-cart-v1" if.bind="!bulkcart" data-widget="ph-add-to-cart-v1" job-detail.bind="eachResult" class="ph-add-to-cart-v1-default-default" view="view1"></div>-->
#                                                                     <div class="savejob-checkbox" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-lWmxkg">
#                                                                         <label data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-eySiqX" class="au-target" au-target-id="307" for="save-625478-4">
#                                                                             <input type="checkbox" checked.bind="eachResult.isJobSaved" change.delegate="handleSaveJob(eachResult)" role="checkbox" data-ph-at-id="save-click" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LoOray" class="au-target" au-target-id="308" id="save-625478-4" aria-label="Save Support Engineer job ID 625478 to job cart" aria-checked="false">
#                                                                             <span class="label-content" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5iZTnr">
#                                                                                 <i class="icon icon-star-empty" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-3hSiPg"></i>
#                                                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSaveText" data-ph-at-id="save-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-V3uiSa">
#                 Save
#                </ppc-content>
#                                                                             </span><!--anchor-->
#                                                                             <!--anchor-->
#                                                                         </label>
#                                                                     </div><!--anchor-->
#                                                                 </div>
#                                                                  <!--End Job saved block -->
#                                                             </div>
#                                                         </div>
#                                                     </li><li class="jobs-list-item" data-ph-at-id="jobs-list-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-y4hTr0">
#                                                         <div class="information-block row" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-zEw2pE">
#                                                             <div class="left-block col-xs-12 col-md-10" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-rmeHWW">
#                                                                 <!-- jobs link block -->
#                                                                 <div class="information" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-fm9Dgs">
#                                                                     <a focus.bind="$index == 0 &amp;&amp; currentSelectedPage > 1" ph-tevent="job_click" ref="linkEle" role="link" key-role="2fssdu-ph-search-results-v1-view-external-linkRole" target="_blank" data-ph-at-id="job-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ic7VNu" class="au-target" au-target-id="288" ph-click-ctx="job" ph-tref="1569669868433175b1" ph-tag="ph-search-results-v1" href="https://careers.microsoft.com/us/en/job/683146/Support-Escalation-Engineer" aria-label="Support Escalation Engineer job ID 683146 opens in a new tab" data-ph-at-job-title-text="Support Escalation Engineer" data-ph-at-job-location-text="San Jose, San José, Costa Rica" data-ph-at-job-category-text="Services" data-ph-at-job-id-text="683146" data-ph-at-job-type-text="" data-ph-at-job-industry-text="" data-ph-at-job-post-date-text="2019-08-05T21:56:00" data-ph-at-job-seqno-text="683146" data-ph-at-job-position-text="" data-ph-at-job-employment-type-text="" data-ph-at-job-role-type-text="" data-ph-at-job-education-level-text="">
#                                                                         <span class="job-title" data-ph-at-id="searchresults-job-title" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-MRnq6A">Support Escalation Engineer</span>
#                                                                     </a>
#                                                                     <div class="job-additional-info" data-ph-at-id="job-info" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LesJKv">
#                                                                         <span class="job-location" data-ph-at-id="searchresults-job-location" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CQMOUl">
#                                                                             San Jose, San José, Costa Rica
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-category" data-ph-at-id="searchresults-job-category" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-g94YTa">
#                                                                             Services
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-date au-target" data-ph-at-id="searchresults-job-postdate" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-b6UGw3" au-target-id="294" aria-label="Aug 5th 2019">
#                                                                             Aug 5, 2019
#                                                                         </span><!--anchor-->
#                                                                     </div>
#                                                                     <div class="description au-target" innerhtml.bind="eachResult.descriptionTeaser | sanitizeHTML" data-ph-at-id="jobdescription-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Abw08f" au-target-id="297">Are you interested in the cloud business and enabling Linux OSS workloads? The Microsoft Azure Platform is strategic to Microsoft enabling customers, ISVs, and Microsoft IT to develop, test, and</div>
#                                                                 </div>
#                                                                 <!--End jobs link block -->
#
#                                                                 <!-- jobs multilocation block -->
#                                                                 <!--anchor-->
#                                                                 <!--End jobs multilocation block -->
#                                                             </div>
#                                                             <div class="right-block col-xs-12 col-md-2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-W9vvx1">
#                                                                 <!-- Job applied status block -->
#                                                                 <div class="applied-action" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0WA3mP">
#                                                                     <section class="ph-widget" instance-id="we3alx" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CGkAfP" view="1565777110184-default" original-view="default" theme="default">
#                                                                         <div as-element="ph-job-status-v1" arrjoblist.bind="$index===0 ? jobResults : null" jobid="${eachResult.jobSeqNo}" view="1565777110184-default" mode="APPLY" class="ph-job-status-v1-default-default ph-widget-target au-target" data-widget="ph-job-status-v1" instance-id="we3alx" original-view="default" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TWsAYD" au-target-id="306">
#
#                                                                             <!--anchor-->
#                                                                         <!--anchor--></div>
#                                                                     </section>
#                                                                 </div>
#                                                                 <!--End Job applied status block -->
#
#                                                                 <!-- Job saved block -->
#                                                                 <div class="actions" data-ph-at-id="job-actions" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Kt42DX">
#                                                                     <!--<div as-element="ph-add-to-cart-v1" if.bind="!bulkcart" data-widget="ph-add-to-cart-v1" job-detail.bind="eachResult" class="ph-add-to-cart-v1-default-default" view="view1"></div>-->
#                                                                     <div class="savejob-checkbox" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-lWmxkg">
#                                                                         <label data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-eySiqX" class="au-target" au-target-id="307" for="save-683146-5">
#                                                                             <input type="checkbox" checked.bind="eachResult.isJobSaved" change.delegate="handleSaveJob(eachResult)" role="checkbox" data-ph-at-id="save-click" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LoOray" class="au-target" au-target-id="308" id="save-683146-5" aria-label="Save Support Escalation Engineer job ID 683146 to job cart" aria-checked="false">
#                                                                             <span class="label-content" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5iZTnr">
#                                                                                 <i class="icon icon-star-empty" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-3hSiPg"></i>
#                                                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSaveText" data-ph-at-id="save-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-V3uiSa">
#                 Save
#                </ppc-content>
#                                                                             </span><!--anchor-->
#                                                                             <!--anchor-->
#                                                                         </label>
#                                                                     </div><!--anchor-->
#                                                                 </div>
#                                                                  <!--End Job saved block -->
#                                                             </div>
#                                                         </div>
#                                                     </li><li class="jobs-list-item" data-ph-at-id="jobs-list-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-y4hTr0">
#                                                         <div class="information-block row" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-zEw2pE">
#                                                             <div class="left-block col-xs-12 col-md-10" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-rmeHWW">
#                                                                 <!-- jobs link block -->
#                                                                 <div class="information" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-fm9Dgs">
#                                                                     <a focus.bind="$index == 0 &amp;&amp; currentSelectedPage > 1" ph-tevent="job_click" ref="linkEle" role="link" key-role="2fssdu-ph-search-results-v1-view-external-linkRole" target="_blank" data-ph-at-id="job-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ic7VNu" class="au-target" au-target-id="288" ph-click-ctx="job" ph-tref="156966986843318a98" ph-tag="ph-search-results-v1" href="https://careers.microsoft.com/us/en/job/700066/Sales-Solution-Specialist-Digital-Sales-Norwegian-Finnish-Dutch-German-Danish-and-Swedish-languages" aria-label="Sales Solution Specialist - Digital Sales. Norwegian, Finnish, Dutch, German, Danish and Swedish languages job ID 700066 opens in a new tab" data-ph-at-job-title-text="Sales Solution Specialist - Digital Sales. Norwegian, Finnish, Dutch, German, Danish and Swedish languages" data-ph-at-job-location-text="Dublin, Dublin, Ireland" data-ph-at-job-category-text="Sales" data-ph-at-job-id-text="700066" data-ph-at-job-type-text="" data-ph-at-job-industry-text="" data-ph-at-job-post-date-text="2019-09-05T10:03:00" data-ph-at-job-seqno-text="700066" data-ph-at-job-position-text="" data-ph-at-job-employment-type-text="" data-ph-at-job-role-type-text="" data-ph-at-job-education-level-text="">
#                                                                         <span class="job-title" data-ph-at-id="searchresults-job-title" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-MRnq6A">Sales Solution Specialist - Digital Sales. Norwegian, Finnish, Dutch, German, Danish and Swedish languages</span>
#                                                                     </a>
#                                                                     <div class="job-additional-info" data-ph-at-id="job-info" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LesJKv">
#                                                                         <span class="job-location" data-ph-at-id="searchresults-job-location" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CQMOUl">
#                                                                             Dublin, Dublin, Ireland
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-category" data-ph-at-id="searchresults-job-category" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-g94YTa">
#                                                                             Sales
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-date au-target" data-ph-at-id="searchresults-job-postdate" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-b6UGw3" au-target-id="294" aria-label="Sep 5th 2019">
#                                                                             Sep 5, 2019
#                                                                         </span><!--anchor-->
#                                                                     </div>
#                                                                     <div class="description au-target" innerhtml.bind="eachResult.descriptionTeaser | sanitizeHTML" data-ph-at-id="jobdescription-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Abw08f" au-target-id="297">Microsoft is empowering every person and every organization on the planet to do more and achieve more. We have set ourselves three bold ambitions: create more personal computing, reinvent productivity</div>
#                                                                 </div>
#                                                                 <!--End jobs link block -->
#
#                                                                 <!-- jobs multilocation block -->
#                                                                 <!--anchor-->
#                                                                 <!--End jobs multilocation block -->
#                                                             </div>
#                                                             <div class="right-block col-xs-12 col-md-2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-W9vvx1">
#                                                                 <!-- Job applied status block -->
#                                                                 <div class="applied-action" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0WA3mP">
#                                                                     <section class="ph-widget" instance-id="we3alx" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CGkAfP" view="1565777110184-default" original-view="default" theme="default">
#                                                                         <div as-element="ph-job-status-v1" arrjoblist.bind="$index===0 ? jobResults : null" jobid="${eachResult.jobSeqNo}" view="1565777110184-default" mode="APPLY" class="ph-job-status-v1-default-default ph-widget-target au-target" data-widget="ph-job-status-v1" instance-id="we3alx" original-view="default" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TWsAYD" au-target-id="306">
#
#                                                                             <!--anchor-->
#                                                                         <!--anchor--></div>
#                                                                     </section>
#                                                                 </div>
#                                                                 <!--End Job applied status block -->
#
#                                                                 <!-- Job saved block -->
#                                                                 <div class="actions" data-ph-at-id="job-actions" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Kt42DX">
#                                                                     <!--<div as-element="ph-add-to-cart-v1" if.bind="!bulkcart" data-widget="ph-add-to-cart-v1" job-detail.bind="eachResult" class="ph-add-to-cart-v1-default-default" view="view1"></div>-->
#                                                                     <div class="savejob-checkbox" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-lWmxkg">
#                                                                         <label data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-eySiqX" class="au-target" au-target-id="307" for="save-700066-6">
#                                                                             <input type="checkbox" checked.bind="eachResult.isJobSaved" change.delegate="handleSaveJob(eachResult)" role="checkbox" data-ph-at-id="save-click" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LoOray" class="au-target" au-target-id="308" id="save-700066-6" aria-label="Save Sales Solution Specialist - Digital Sales. Norwegian, Finnish, Dutch, German, Danish and Swedish languages job ID 700066 to job cart" aria-checked="false">
#                                                                             <span class="label-content" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5iZTnr">
#                                                                                 <i class="icon icon-star-empty" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-3hSiPg"></i>
#                                                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSaveText" data-ph-at-id="save-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-V3uiSa">
#                 Save
#                </ppc-content>
#                                                                             </span><!--anchor-->
#                                                                             <!--anchor-->
#                                                                         </label>
#                                                                     </div><!--anchor-->
#                                                                 </div>
#                                                                  <!--End Job saved block -->
#                                                             </div>
#                                                         </div>
#                                                     </li><li class="jobs-list-item" data-ph-at-id="jobs-list-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-y4hTr0">
#                                                         <div class="information-block row" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-zEw2pE">
#                                                             <div class="left-block col-xs-12 col-md-10" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-rmeHWW">
#                                                                 <!-- jobs link block -->
#                                                                 <div class="information" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-fm9Dgs">
#                                                                     <a focus.bind="$index == 0 &amp;&amp; currentSelectedPage > 1" ph-tevent="job_click" ref="linkEle" role="link" key-role="2fssdu-ph-search-results-v1-view-external-linkRole" target="_blank" data-ph-at-id="job-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ic7VNu" class="au-target" au-target-id="288" ph-click-ctx="job" ph-tref="156966986843412d20" ph-tag="ph-search-results-v1" href="https://careers.microsoft.com/us/en/job/684810/Support-Escalation-Engineer" aria-label="Support Escalation Engineer job ID 684810 opens in a new tab" data-ph-at-job-title-text="Support Escalation Engineer" data-ph-at-job-location-text="Las Colinas, Texas, United States" data-ph-at-job-category-text="Services" data-ph-at-job-id-text="684810" data-ph-at-job-type-text="" data-ph-at-job-industry-text="" data-ph-at-job-post-date-text="2019-08-08T21:41:00" data-ph-at-job-seqno-text="684810" data-ph-at-job-position-text="" data-ph-at-job-employment-type-text="" data-ph-at-job-role-type-text="" data-ph-at-job-education-level-text="">
#                                                                         <span class="job-title" data-ph-at-id="searchresults-job-title" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-MRnq6A">Support Escalation Engineer</span>
#                                                                     </a>
#                                                                     <div class="job-additional-info" data-ph-at-id="job-info" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LesJKv">
#                                                                         <!--anchor-->
#                                                                         <span class="job-category" data-ph-at-id="searchresults-job-category" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-g94YTa">
#                                                                             Services
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-date au-target" data-ph-at-id="searchresults-job-postdate" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-b6UGw3" au-target-id="294" aria-label="Aug 8th 2019">
#                                                                             Aug 8, 2019
#                                                                         </span><!--anchor-->
#                                                                     </div>
#                                                                     <div class="description au-target" innerhtml.bind="eachResult.descriptionTeaser | sanitizeHTML" data-ph-at-id="jobdescription-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Abw08f" au-target-id="297">Are you interested in the cloud business and enabling Linux OSS workloads? The Microsoft Azure Platform is strategic to Microsoft enabling customers, ISVs, and Microsoft IT to develop, test, and</div>
#                                                                 </div>
#                                                                 <!--End jobs link block -->
#
#                                                                 <!-- jobs multilocation block -->
#                                                                 <div class="job-multi-locations" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-vJOVzG">
#                                                                     <button ph-tevent="multi_location_click" keyup.trigger="($event.keyCode === 27)?(eachResult.toggleOpen = false):''" class="esc$$close au-target" click.delegate="eachResult.toggleOpen = !eachResult.toggleOpen" role="button" key-role="IWwth6-2fssdu-ph-search-results-v1-view-external-btnRole" data-ph-at-id="job-multi-locations-button" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0aUp1e" au-target-id="298" data-ph-tevent-attr-trait14="Services" data-ph-tevent-attr-trait5="684810" id="searchLoc-7" aria-expanded="false" aria-label="Support Escalation Engineer job ID 684810 Job available in 2 locations" data-ph-at-job-multilocation-count="2">
#                                                                         <span data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-h6pjaT"><ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultJobAvailText1" data-ph-at-id="multilocation-text1" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5DjjWH">
#               Job available in
#              </ppc-content></span> 2 <span data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5Lm1HA"><ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultJobAvailText2" data-ph-at-id="multilocation-text2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-2Go8OT">
#               locations
#              </ppc-content></span>
#                                                                         <!--icon toggle based on item click: js dependent-->
#                                                                         <!--<i ref="listItemIcon" class="icon icon-down-arrow" aria-hidden="true"></i>-->
#                                                                         <i ref="listItemIcon" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-KotPHt" class="au-target icon icon-down-arrow" au-target-id="300"></i>
#                                                                     </button>
#                                                                     <!--dropView used to toggle toggleMultiLocationView based on item click: js dependent-->
#                                                                     <ul ref="listItem" data-ph-at-id="job-multi-locations-list" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-cbms8u" class="au-target hide" au-target-id="301" aria-hidden="true">
#                                                                         <li class="location au-target" data-ph-at-id="job-multi-location-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-EgsS0Q" au-target-id="302" aria-label="Las Colinas, Texas, United States" data-ph-at-job-location-text="Las Colinas, Texas, United States">
#                                                                             Las Colinas, Texas, United States
#                                                                         </li><li class="location au-target" data-ph-at-id="job-multi-location-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-EgsS0Q" au-target-id="302" aria-label="Charlotte, North Carolina, United States" data-ph-at-job-location-text="Charlotte, North Carolina, United States">
#                                                                             Charlotte, North Carolina, United States
#                                                                         </li><!--anchor-->
#                                                                     </ul>
#                                                                 </div><!--anchor-->
#                                                                 <!--End jobs multilocation block -->
#                                                             </div>
#                                                             <div class="right-block col-xs-12 col-md-2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-W9vvx1">
#                                                                 <!-- Job applied status block -->
#                                                                 <div class="applied-action" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0WA3mP">
#                                                                     <section class="ph-widget" instance-id="we3alx" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CGkAfP" view="1565777110184-default" original-view="default" theme="default">
#                                                                         <div as-element="ph-job-status-v1" arrjoblist.bind="$index===0 ? jobResults : null" jobid="${eachResult.jobSeqNo}" view="1565777110184-default" mode="APPLY" class="ph-job-status-v1-default-default ph-widget-target au-target" data-widget="ph-job-status-v1" instance-id="we3alx" original-view="default" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TWsAYD" au-target-id="306">
#
#                                                                             <!--anchor-->
#                                                                         <!--anchor--></div>
#                                                                     </section>
#                                                                 </div>
#                                                                 <!--End Job applied status block -->
#
#                                                                 <!-- Job saved block -->
#                                                                 <div class="actions" data-ph-at-id="job-actions" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Kt42DX">
#                                                                     <!--<div as-element="ph-add-to-cart-v1" if.bind="!bulkcart" data-widget="ph-add-to-cart-v1" job-detail.bind="eachResult" class="ph-add-to-cart-v1-default-default" view="view1"></div>-->
#                                                                     <div class="savejob-checkbox" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-lWmxkg">
#                                                                         <label data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-eySiqX" class="au-target" au-target-id="307" for="save-684810-7">
#                                                                             <input type="checkbox" checked.bind="eachResult.isJobSaved" change.delegate="handleSaveJob(eachResult)" role="checkbox" data-ph-at-id="save-click" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LoOray" class="au-target" au-target-id="308" id="save-684810-7" aria-label="Save Support Escalation Engineer job ID 684810 to job cart" aria-checked="false">
#                                                                             <span class="label-content" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5iZTnr">
#                                                                                 <i class="icon icon-star-empty" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-3hSiPg"></i>
#                                                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSaveText" data-ph-at-id="save-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-V3uiSa">
#                 Save
#                </ppc-content>
#                                                                             </span><!--anchor-->
#                                                                             <!--anchor-->
#                                                                         </label>
#                                                                     </div><!--anchor-->
#                                                                 </div>
#                                                                  <!--End Job saved block -->
#                                                             </div>
#                                                         </div>
#                                                     </li><li class="jobs-list-item" data-ph-at-id="jobs-list-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-y4hTr0">
#                                                         <div class="information-block row" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-zEw2pE">
#                                                             <div class="left-block col-xs-12 col-md-10" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-rmeHWW">
#                                                                 <!-- jobs link block -->
#                                                                 <div class="information" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-fm9Dgs">
#                                                                     <a focus.bind="$index == 0 &amp;&amp; currentSelectedPage > 1" ph-tevent="job_click" ref="linkEle" role="link" key-role="2fssdu-ph-search-results-v1-view-external-linkRole" target="_blank" data-ph-at-id="job-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ic7VNu" class="au-target" au-target-id="288" ph-click-ctx="job" ph-tref="1569669868434165f1" ph-tag="ph-search-results-v1" href="https://careers.microsoft.com/us/en/job/623537/Support-Escalation-Engineer-Azure-Rapid-Response" aria-label="Support Escalation Engineer - Azure Rapid Response job ID 623537 opens in a new tab" data-ph-at-job-title-text="Support Escalation Engineer - Azure Rapid Response" data-ph-at-job-location-text="Seoul, Seoul, Korea" data-ph-at-job-category-text="Services" data-ph-at-job-id-text="623537" data-ph-at-job-type-text="" data-ph-at-job-industry-text="" data-ph-at-job-post-date-text="2019-08-09T08:57:00" data-ph-at-job-seqno-text="623537" data-ph-at-job-position-text="" data-ph-at-job-employment-type-text="" data-ph-at-job-role-type-text="" data-ph-at-job-education-level-text="">
#                                                                         <span class="job-title" data-ph-at-id="searchresults-job-title" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-MRnq6A">Support Escalation Engineer - Azure Rapid Response</span>
#                                                                     </a>
#                                                                     <div class="job-additional-info" data-ph-at-id="job-info" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LesJKv">
#                                                                         <span class="job-location" data-ph-at-id="searchresults-job-location" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CQMOUl">
#                                                                             Seoul, Seoul, Korea
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-category" data-ph-at-id="searchresults-job-category" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-g94YTa">
#                                                                             Services
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-date au-target" data-ph-at-id="searchresults-job-postdate" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-b6UGw3" au-target-id="294" aria-label="Aug 9th 2019">
#                                                                             Aug 9, 2019
#                                                                         </span><!--anchor-->
#                                                                     </div>
#                                                                     <div class="description au-target" innerhtml.bind="eachResult.descriptionTeaser | sanitizeHTML" data-ph-at-id="jobdescription-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Abw08f" au-target-id="297">As cloud goes main stream, Azure leads the way. Azure's continued success depends on providing customers a world class support experience. Love services, support in the cloud? Customer obsessed? Data</div>
#                                                                 </div>
#                                                                 <!--End jobs link block -->
#
#                                                                 <!-- jobs multilocation block -->
#                                                                 <!--anchor-->
#                                                                 <!--End jobs multilocation block -->
#                                                             </div>
#                                                             <div class="right-block col-xs-12 col-md-2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-W9vvx1">
#                                                                 <!-- Job applied status block -->
#                                                                 <div class="applied-action" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0WA3mP">
#                                                                     <section class="ph-widget" instance-id="we3alx" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CGkAfP" view="1565777110184-default" original-view="default" theme="default">
#                                                                         <div as-element="ph-job-status-v1" arrjoblist.bind="$index===0 ? jobResults : null" jobid="${eachResult.jobSeqNo}" view="1565777110184-default" mode="APPLY" class="ph-job-status-v1-default-default ph-widget-target au-target" data-widget="ph-job-status-v1" instance-id="we3alx" original-view="default" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TWsAYD" au-target-id="306">
#
#                                                                             <!--anchor-->
#                                                                         <!--anchor--></div>
#                                                                     </section>
#                                                                 </div>
#                                                                 <!--End Job applied status block -->
#
#                                                                 <!-- Job saved block -->
#                                                                 <div class="actions" data-ph-at-id="job-actions" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Kt42DX">
#                                                                     <!--<div as-element="ph-add-to-cart-v1" if.bind="!bulkcart" data-widget="ph-add-to-cart-v1" job-detail.bind="eachResult" class="ph-add-to-cart-v1-default-default" view="view1"></div>-->
#                                                                     <div class="savejob-checkbox" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-lWmxkg">
#                                                                         <label data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-eySiqX" class="au-target" au-target-id="307" for="save-623537-8">
#                                                                             <input type="checkbox" checked.bind="eachResult.isJobSaved" change.delegate="handleSaveJob(eachResult)" role="checkbox" data-ph-at-id="save-click" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LoOray" class="au-target" au-target-id="308" id="save-623537-8" aria-label="Save Support Escalation Engineer - Azure Rapid Response job ID 623537 to job cart" aria-checked="false">
#                                                                             <span class="label-content" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5iZTnr">
#                                                                                 <i class="icon icon-star-empty" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-3hSiPg"></i>
#                                                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSaveText" data-ph-at-id="save-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-V3uiSa">
#                 Save
#                </ppc-content>
#                                                                             </span><!--anchor-->
#                                                                             <!--anchor-->
#                                                                         </label>
#                                                                     </div><!--anchor-->
#                                                                 </div>
#                                                                  <!--End Job saved block -->
#                                                             </div>
#                                                         </div>
#                                                     </li><li class="jobs-list-item" data-ph-at-id="jobs-list-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-y4hTr0">
#                                                         <div class="information-block row" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-zEw2pE">
#                                                             <div class="left-block col-xs-12 col-md-10" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-rmeHWW">
#                                                                 <!-- jobs link block -->
#                                                                 <div class="information" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-fm9Dgs">
#                                                                     <a focus.bind="$index == 0 &amp;&amp; currentSelectedPage > 1" ph-tevent="job_click" ref="linkEle" role="link" key-role="2fssdu-ph-search-results-v1-view-external-linkRole" target="_blank" data-ph-at-id="job-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ic7VNu" class="au-target" au-target-id="288" ph-click-ctx="job" ph-tref="156966986843515132" ph-tag="ph-search-results-v1" href="https://careers.microsoft.com/us/en/job/592315/Support-Escalation-Engineer" aria-label="Support Escalation Engineer job ID 592315 opens in a new tab" data-ph-at-job-title-text="Support Escalation Engineer" data-ph-at-job-location-text="Bangalore, Karnataka, India" data-ph-at-job-category-text="Services" data-ph-at-job-id-text="592315" data-ph-at-job-type-text="" data-ph-at-job-industry-text="" data-ph-at-job-post-date-text="2019-07-01T12:43:00" data-ph-at-job-seqno-text="592315" data-ph-at-job-position-text="" data-ph-at-job-employment-type-text="" data-ph-at-job-role-type-text="" data-ph-at-job-education-level-text="">
#                                                                         <span class="job-title" data-ph-at-id="searchresults-job-title" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-MRnq6A">Support Escalation Engineer</span>
#                                                                     </a>
#                                                                     <div class="job-additional-info" data-ph-at-id="job-info" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LesJKv">
#                                                                         <span class="job-location" data-ph-at-id="searchresults-job-location" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CQMOUl">
#                                                                             Bangalore, Karnataka, India
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-category" data-ph-at-id="searchresults-job-category" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-g94YTa">
#                                                                             Services
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-date au-target" data-ph-at-id="searchresults-job-postdate" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-b6UGw3" au-target-id="294" aria-label="Jul 1st 2019">
#                                                                             Jul 1, 2019
#                                                                         </span><!--anchor-->
#                                                                     </div>
#                                                                     <div class="description au-target" innerhtml.bind="eachResult.descriptionTeaser | sanitizeHTML" data-ph-at-id="jobdescription-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Abw08f" au-target-id="297">As cloud goes main stream, Azure leads the way. Azure's continued success depends on providing customers a world class support experience. Love services, support in the cloud? Customer obsessed? Data</div>
#                                                                 </div>
#                                                                 <!--End jobs link block -->
#
#                                                                 <!-- jobs multilocation block -->
#                                                                 <!--anchor-->
#                                                                 <!--End jobs multilocation block -->
#                                                             </div>
#                                                             <div class="right-block col-xs-12 col-md-2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-W9vvx1">
#                                                                 <!-- Job applied status block -->
#                                                                 <div class="applied-action" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0WA3mP">
#                                                                     <section class="ph-widget" instance-id="we3alx" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CGkAfP" view="1565777110184-default" original-view="default" theme="default">
#                                                                         <div as-element="ph-job-status-v1" arrjoblist.bind="$index===0 ? jobResults : null" jobid="${eachResult.jobSeqNo}" view="1565777110184-default" mode="APPLY" class="ph-job-status-v1-default-default ph-widget-target au-target" data-widget="ph-job-status-v1" instance-id="we3alx" original-view="default" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TWsAYD" au-target-id="306">
#
#                                                                             <!--anchor-->
#                                                                         <!--anchor--></div>
#                                                                     </section>
#                                                                 </div>
#                                                                 <!--End Job applied status block -->
#
#                                                                 <!-- Job saved block -->
#                                                                 <div class="actions" data-ph-at-id="job-actions" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Kt42DX">
#                                                                     <!--<div as-element="ph-add-to-cart-v1" if.bind="!bulkcart" data-widget="ph-add-to-cart-v1" job-detail.bind="eachResult" class="ph-add-to-cart-v1-default-default" view="view1"></div>-->
#                                                                     <div class="savejob-checkbox" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-lWmxkg">
#                                                                         <label data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-eySiqX" class="au-target" au-target-id="307" for="save-592315-9">
#                                                                             <input type="checkbox" checked.bind="eachResult.isJobSaved" change.delegate="handleSaveJob(eachResult)" role="checkbox" data-ph-at-id="save-click" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LoOray" class="au-target" au-target-id="308" id="save-592315-9" aria-label="Save Support Escalation Engineer job ID 592315 to job cart" aria-checked="false">
#                                                                             <span class="label-content" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5iZTnr">
#                                                                                 <i class="icon icon-star-empty" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-3hSiPg"></i>
#                                                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSaveText" data-ph-at-id="save-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-V3uiSa">
#                 Save
#                </ppc-content>
#                                                                             </span><!--anchor-->
#                                                                             <!--anchor-->
#                                                                         </label>
#                                                                     </div><!--anchor-->
#                                                                 </div>
#                                                                  <!--End Job saved block -->
#                                                             </div>
#                                                         </div>
#                                                     </li><li class="jobs-list-item" data-ph-at-id="jobs-list-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-y4hTr0">
#                                                         <div class="information-block row" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-zEw2pE">
#                                                             <div class="left-block col-xs-12 col-md-10" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-rmeHWW">
#                                                                 <!-- jobs link block -->
#                                                                 <div class="information" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-fm9Dgs">
#                                                                     <a focus.bind="$index == 0 &amp;&amp; currentSelectedPage > 1" ph-tevent="job_click" ref="linkEle" role="link" key-role="2fssdu-ph-search-results-v1-view-external-linkRole" target="_blank" data-ph-at-id="job-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ic7VNu" class="au-target" au-target-id="288" ph-click-ctx="job" ph-tref="15696698684351f0dc" ph-tag="ph-search-results-v1" href="https://careers.microsoft.com/us/en/job/664725/Support-Escalation-Engineer-Azure-Rapid-Response" aria-label="Support Escalation Engineer_Azure Rapid Response job ID 664725 opens in a new tab" data-ph-at-job-title-text="Support Escalation Engineer_Azure Rapid Response" data-ph-at-job-location-text="Shanghai, Shanghai, China" data-ph-at-job-category-text="Services" data-ph-at-job-id-text="664725" data-ph-at-job-type-text="" data-ph-at-job-industry-text="" data-ph-at-job-post-date-text="2019-07-17T12:55:00" data-ph-at-job-seqno-text="664725" data-ph-at-job-position-text="" data-ph-at-job-employment-type-text="" data-ph-at-job-role-type-text="" data-ph-at-job-education-level-text="">
#                                                                         <span class="job-title" data-ph-at-id="searchresults-job-title" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-MRnq6A">Support Escalation Engineer_Azure Rapid Response</span>
#                                                                     </a>
#                                                                     <div class="job-additional-info" data-ph-at-id="job-info" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LesJKv">
#                                                                         <span class="job-location" data-ph-at-id="searchresults-job-location" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CQMOUl">
#                                                                             Shanghai, Shanghai, China
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-category" data-ph-at-id="searchresults-job-category" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-g94YTa">
#                                                                             Services
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-date au-target" data-ph-at-id="searchresults-job-postdate" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-b6UGw3" au-target-id="294" aria-label="Jul 17th 2019">
#                                                                             Jul 17, 2019
#                                                                         </span><!--anchor-->
#                                                                     </div>
#                                                                     <div class="description au-target" innerhtml.bind="eachResult.descriptionTeaser | sanitizeHTML" data-ph-at-id="jobdescription-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Abw08f" au-target-id="297">• As cloud goes main stream, Azure leads the way. Azure's continued success depends on providing customers a world class support experience. Love services, support in the cloud? Customer</div>
#                                                                 </div>
#                                                                 <!--End jobs link block -->
#
#                                                                 <!-- jobs multilocation block -->
#                                                                 <!--anchor-->
#                                                                 <!--End jobs multilocation block -->
#                                                             </div>
#                                                             <div class="right-block col-xs-12 col-md-2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-W9vvx1">
#                                                                 <!-- Job applied status block -->
#                                                                 <div class="applied-action" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0WA3mP">
#                                                                     <section class="ph-widget" instance-id="we3alx" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CGkAfP" view="1565777110184-default" original-view="default" theme="default">
#                                                                         <div as-element="ph-job-status-v1" arrjoblist.bind="$index===0 ? jobResults : null" jobid="${eachResult.jobSeqNo}" view="1565777110184-default" mode="APPLY" class="ph-job-status-v1-default-default ph-widget-target au-target" data-widget="ph-job-status-v1" instance-id="we3alx" original-view="default" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TWsAYD" au-target-id="306">
#
#                                                                             <!--anchor-->
#                                                                         <!--anchor--></div>
#                                                                     </section>
#                                                                 </div>
#                                                                 <!--End Job applied status block -->
#
#                                                                 <!-- Job saved block -->
#                                                                 <div class="actions" data-ph-at-id="job-actions" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Kt42DX">
#                                                                     <!--<div as-element="ph-add-to-cart-v1" if.bind="!bulkcart" data-widget="ph-add-to-cart-v1" job-detail.bind="eachResult" class="ph-add-to-cart-v1-default-default" view="view1"></div>-->
#                                                                     <div class="savejob-checkbox" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-lWmxkg">
#                                                                         <label data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-eySiqX" class="au-target" au-target-id="307" for="save-664725-10">
#                                                                             <input type="checkbox" checked.bind="eachResult.isJobSaved" change.delegate="handleSaveJob(eachResult)" role="checkbox" data-ph-at-id="save-click" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LoOray" class="au-target" au-target-id="308" id="save-664725-10" aria-label="Save Support Escalation Engineer_Azure Rapid Response job ID 664725 to job cart" aria-checked="false">
#                                                                             <span class="label-content" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5iZTnr">
#                                                                                 <i class="icon icon-star-empty" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-3hSiPg"></i>
#                                                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSaveText" data-ph-at-id="save-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-V3uiSa">
#                 Save
#                </ppc-content>
#                                                                             </span><!--anchor-->
#                                                                             <!--anchor-->
#                                                                         </label>
#                                                                     </div><!--anchor-->
#                                                                 </div>
#                                                                  <!--End Job saved block -->
#                                                             </div>
#                                                         </div>
#                                                     </li><li class="jobs-list-item" data-ph-at-id="jobs-list-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-y4hTr0">
#                                                         <div class="information-block row" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-zEw2pE">
#                                                             <div class="left-block col-xs-12 col-md-10" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-rmeHWW">
#                                                                 <!-- jobs link block -->
#                                                                 <div class="information" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-fm9Dgs">
#                                                                     <a focus.bind="$index == 0 &amp;&amp; currentSelectedPage > 1" ph-tevent="job_click" ref="linkEle" role="link" key-role="2fssdu-ph-search-results-v1-view-external-linkRole" target="_blank" data-ph-at-id="job-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ic7VNu" class="au-target" au-target-id="288" ph-click-ctx="job" ph-tref="15696698684351fef4" ph-tag="ph-search-results-v1" href="https://careers.microsoft.com/us/en/job/701815/Support-Escalation-Engineer" aria-label="Support Escalation Engineer job ID 701815 opens in a new tab" data-ph-at-job-title-text="Support Escalation Engineer" data-ph-at-job-location-text="Hyderabad, Telangana, India" data-ph-at-job-category-text="Services" data-ph-at-job-id-text="701815" data-ph-at-job-type-text="" data-ph-at-job-industry-text="" data-ph-at-job-post-date-text="2019-09-09T11:53:00" data-ph-at-job-seqno-text="701815" data-ph-at-job-position-text="" data-ph-at-job-employment-type-text="" data-ph-at-job-role-type-text="" data-ph-at-job-education-level-text="">
#                                                                         <span class="job-title" data-ph-at-id="searchresults-job-title" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-MRnq6A">Support Escalation Engineer</span>
#                                                                     </a>
#                                                                     <div class="job-additional-info" data-ph-at-id="job-info" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LesJKv">
#                                                                         <span class="job-location" data-ph-at-id="searchresults-job-location" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CQMOUl">
#                                                                             Hyderabad, Telangana, India
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-category" data-ph-at-id="searchresults-job-category" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-g94YTa">
#                                                                             Services
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-date au-target" data-ph-at-id="searchresults-job-postdate" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-b6UGw3" au-target-id="294" aria-label="Sep 9th 2019">
#                                                                             Sep 9, 2019
#                                                                         </span><!--anchor-->
#                                                                     </div>
#                                                                     <div class="description au-target" innerhtml.bind="eachResult.descriptionTeaser | sanitizeHTML" data-ph-at-id="jobdescription-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Abw08f" au-target-id="297">As cloud goes main stream, Azure leads the way. Azure's continued success depends on providing customers a world class support experience. Love services, support in the cloud? Customer obsessed? Data</div>
#                                                                 </div>
#                                                                 <!--End jobs link block -->
#
#                                                                 <!-- jobs multilocation block -->
#                                                                 <!--anchor-->
#                                                                 <!--End jobs multilocation block -->
#                                                             </div>
#                                                             <div class="right-block col-xs-12 col-md-2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-W9vvx1">
#                                                                 <!-- Job applied status block -->
#                                                                 <div class="applied-action" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0WA3mP">
#                                                                     <section class="ph-widget" instance-id="we3alx" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CGkAfP" view="1565777110184-default" original-view="default" theme="default">
#                                                                         <div as-element="ph-job-status-v1" arrjoblist.bind="$index===0 ? jobResults : null" jobid="${eachResult.jobSeqNo}" view="1565777110184-default" mode="APPLY" class="ph-job-status-v1-default-default ph-widget-target au-target" data-widget="ph-job-status-v1" instance-id="we3alx" original-view="default" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TWsAYD" au-target-id="306">
#
#                                                                             <!--anchor-->
#                                                                         <!--anchor--></div>
#                                                                     </section>
#                                                                 </div>
#                                                                 <!--End Job applied status block -->
#
#                                                                 <!-- Job saved block -->
#                                                                 <div class="actions" data-ph-at-id="job-actions" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Kt42DX">
#                                                                     <!--<div as-element="ph-add-to-cart-v1" if.bind="!bulkcart" data-widget="ph-add-to-cart-v1" job-detail.bind="eachResult" class="ph-add-to-cart-v1-default-default" view="view1"></div>-->
#                                                                     <div class="savejob-checkbox" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-lWmxkg">
#                                                                         <label data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-eySiqX" class="au-target" au-target-id="307" for="save-701815-11">
#                                                                             <input type="checkbox" checked.bind="eachResult.isJobSaved" change.delegate="handleSaveJob(eachResult)" role="checkbox" data-ph-at-id="save-click" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LoOray" class="au-target" au-target-id="308" id="save-701815-11" aria-label="Save Support Escalation Engineer job ID 701815 to job cart" aria-checked="false">
#                                                                             <span class="label-content" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5iZTnr">
#                                                                                 <i class="icon icon-star-empty" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-3hSiPg"></i>
#                                                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSaveText" data-ph-at-id="save-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-V3uiSa">
#                 Save
#                </ppc-content>
#                                                                             </span><!--anchor-->
#                                                                             <!--anchor-->
#                                                                         </label>
#                                                                     </div><!--anchor-->
#                                                                 </div>
#                                                                  <!--End Job saved block -->
#                                                             </div>
#                                                         </div>
#                                                     </li><li class="jobs-list-item" data-ph-at-id="jobs-list-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-y4hTr0">
#                                                         <div class="information-block row" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-zEw2pE">
#                                                             <div class="left-block col-xs-12 col-md-10" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-rmeHWW">
#                                                                 <!-- jobs link block -->
#                                                                 <div class="information" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-fm9Dgs">
#                                                                     <a focus.bind="$index == 0 &amp;&amp; currentSelectedPage > 1" ph-tevent="job_click" ref="linkEle" role="link" key-role="2fssdu-ph-search-results-v1-view-external-linkRole" target="_blank" data-ph-at-id="job-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ic7VNu" class="au-target" au-target-id="288" ph-click-ctx="job" ph-tref="1569669868436169f4" ph-tag="ph-search-results-v1" href="https://careers.microsoft.com/us/en/job/690782/Support-Escalation-Engineer" aria-label="Support Escalation Engineer job ID 690782 opens in a new tab" data-ph-at-job-title-text="Support Escalation Engineer" data-ph-at-job-location-text="Hyderabad, Telangana, India" data-ph-at-job-category-text="Services" data-ph-at-job-id-text="690782" data-ph-at-job-type-text="" data-ph-at-job-industry-text="" data-ph-at-job-post-date-text="2019-08-19T08:29:00" data-ph-at-job-seqno-text="690782" data-ph-at-job-position-text="" data-ph-at-job-employment-type-text="" data-ph-at-job-role-type-text="" data-ph-at-job-education-level-text="">
#                                                                         <span class="job-title" data-ph-at-id="searchresults-job-title" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-MRnq6A">Support Escalation Engineer</span>
#                                                                     </a>
#                                                                     <div class="job-additional-info" data-ph-at-id="job-info" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LesJKv">
#                                                                         <span class="job-location" data-ph-at-id="searchresults-job-location" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CQMOUl">
#                                                                             Hyderabad, Telangana, India
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-category" data-ph-at-id="searchresults-job-category" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-g94YTa">
#                                                                             Services
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-date au-target" data-ph-at-id="searchresults-job-postdate" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-b6UGw3" au-target-id="294" aria-label="Aug 19th 2019">
#                                                                             Aug 19, 2019
#                                                                         </span><!--anchor-->
#                                                                     </div>
#                                                                     <div class="description au-target" innerhtml.bind="eachResult.descriptionTeaser | sanitizeHTML" data-ph-at-id="jobdescription-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Abw08f" au-target-id="297">As cloud goes main stream, Azure leads the way. Azure's continued success depends on providing customers a world class support experience. Love services, support in the cloud? Customer obsessed? Data</div>
#                                                                 </div>
#                                                                 <!--End jobs link block -->
#
#                                                                 <!-- jobs multilocation block -->
#                                                                 <!--anchor-->
#                                                                 <!--End jobs multilocation block -->
#                                                             </div>
#                                                             <div class="right-block col-xs-12 col-md-2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-W9vvx1">
#                                                                 <!-- Job applied status block -->
#                                                                 <div class="applied-action" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0WA3mP">
#                                                                     <section class="ph-widget" instance-id="we3alx" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CGkAfP" view="1565777110184-default" original-view="default" theme="default">
#                                                                         <div as-element="ph-job-status-v1" arrjoblist.bind="$index===0 ? jobResults : null" jobid="${eachResult.jobSeqNo}" view="1565777110184-default" mode="APPLY" class="ph-job-status-v1-default-default ph-widget-target au-target" data-widget="ph-job-status-v1" instance-id="we3alx" original-view="default" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TWsAYD" au-target-id="306">
#
#                                                                             <!--anchor-->
#                                                                         <!--anchor--></div>
#                                                                     </section>
#                                                                 </div>
#                                                                 <!--End Job applied status block -->
#
#                                                                 <!-- Job saved block -->
#                                                                 <div class="actions" data-ph-at-id="job-actions" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Kt42DX">
#                                                                     <!--<div as-element="ph-add-to-cart-v1" if.bind="!bulkcart" data-widget="ph-add-to-cart-v1" job-detail.bind="eachResult" class="ph-add-to-cart-v1-default-default" view="view1"></div>-->
#                                                                     <div class="savejob-checkbox" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-lWmxkg">
#                                                                         <label data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-eySiqX" class="au-target" au-target-id="307" for="save-690782-12">
#                                                                             <input type="checkbox" checked.bind="eachResult.isJobSaved" change.delegate="handleSaveJob(eachResult)" role="checkbox" data-ph-at-id="save-click" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LoOray" class="au-target" au-target-id="308" id="save-690782-12" aria-label="Save Support Escalation Engineer job ID 690782 to job cart" aria-checked="false">
#                                                                             <span class="label-content" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5iZTnr">
#                                                                                 <i class="icon icon-star-empty" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-3hSiPg"></i>
#                                                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSaveText" data-ph-at-id="save-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-V3uiSa">
#                 Save
#                </ppc-content>
#                                                                             </span><!--anchor-->
#                                                                             <!--anchor-->
#                                                                         </label>
#                                                                     </div><!--anchor-->
#                                                                 </div>
#                                                                  <!--End Job saved block -->
#                                                             </div>
#                                                         </div>
#                                                     </li><li class="jobs-list-item" data-ph-at-id="jobs-list-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-y4hTr0">
#                                                         <div class="information-block row" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-zEw2pE">
#                                                             <div class="left-block col-xs-12 col-md-10" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-rmeHWW">
#                                                                 <!-- jobs link block -->
#                                                                 <div class="information" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-fm9Dgs">
#                                                                     <a focus.bind="$index == 0 &amp;&amp; currentSelectedPage > 1" ph-tevent="job_click" ref="linkEle" role="link" key-role="2fssdu-ph-search-results-v1-view-external-linkRole" target="_blank" data-ph-at-id="job-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ic7VNu" class="au-target" au-target-id="288" ph-click-ctx="job" ph-tref="1569669868436199e5" ph-tag="ph-search-results-v1" href="https://careers.microsoft.com/us/en/job/653651/Senior-Software-Engineer" aria-label="Senior Software Engineer job ID 653651 opens in a new tab" data-ph-at-job-title-text="Senior Software Engineer" data-ph-at-job-location-text="Redmond, Washington, United States" data-ph-at-job-category-text="Engineering" data-ph-at-job-id-text="653651" data-ph-at-job-type-text="" data-ph-at-job-industry-text="" data-ph-at-job-post-date-text="2019-06-28T18:48:00" data-ph-at-job-seqno-text="653651" data-ph-at-job-position-text="" data-ph-at-job-employment-type-text="" data-ph-at-job-role-type-text="" data-ph-at-job-education-level-text="">
#                                                                         <span class="job-title" data-ph-at-id="searchresults-job-title" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-MRnq6A">Senior Software Engineer</span>
#                                                                     </a>
#                                                                     <div class="job-additional-info" data-ph-at-id="job-info" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LesJKv">
#                                                                         <span class="job-location" data-ph-at-id="searchresults-job-location" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CQMOUl">
#                                                                             Redmond, Washington, United States
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-category" data-ph-at-id="searchresults-job-category" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-g94YTa">
#                                                                             Engineering
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-date au-target" data-ph-at-id="searchresults-job-postdate" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-b6UGw3" au-target-id="294" aria-label="Jun 28th 2019">
#                                                                             Jun 28, 2019
#                                                                         </span><!--anchor-->
#                                                                     </div>
#                                                                     <div class="description au-target" innerhtml.bind="eachResult.descriptionTeaser | sanitizeHTML" data-ph-at-id="jobdescription-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Abw08f" au-target-id="297">The Linux Systems Group is looking for a talented Software Engineer to join our team. If you are interested in working on Linux or open source projects at Microsoft, this is the job for you!</div>
#                                                                 </div>
#                                                                 <!--End jobs link block -->
#
#                                                                 <!-- jobs multilocation block -->
#                                                                 <!--anchor-->
#                                                                 <!--End jobs multilocation block -->
#                                                             </div>
#                                                             <div class="right-block col-xs-12 col-md-2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-W9vvx1">
#                                                                 <!-- Job applied status block -->
#                                                                 <div class="applied-action" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0WA3mP">
#                                                                     <section class="ph-widget" instance-id="we3alx" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CGkAfP" view="1565777110184-default" original-view="default" theme="default">
#                                                                         <div as-element="ph-job-status-v1" arrjoblist.bind="$index===0 ? jobResults : null" jobid="${eachResult.jobSeqNo}" view="1565777110184-default" mode="APPLY" class="ph-job-status-v1-default-default ph-widget-target au-target" data-widget="ph-job-status-v1" instance-id="we3alx" original-view="default" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TWsAYD" au-target-id="306">
#
#                                                                             <!--anchor-->
#                                                                         <!--anchor--></div>
#                                                                     </section>
#                                                                 </div>
#                                                                 <!--End Job applied status block -->
#
#                                                                 <!-- Job saved block -->
#                                                                 <div class="actions" data-ph-at-id="job-actions" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Kt42DX">
#                                                                     <!--<div as-element="ph-add-to-cart-v1" if.bind="!bulkcart" data-widget="ph-add-to-cart-v1" job-detail.bind="eachResult" class="ph-add-to-cart-v1-default-default" view="view1"></div>-->
#                                                                     <div class="savejob-checkbox" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-lWmxkg">
#                                                                         <label data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-eySiqX" class="au-target" au-target-id="307" for="save-653651-13">
#                                                                             <input type="checkbox" checked.bind="eachResult.isJobSaved" change.delegate="handleSaveJob(eachResult)" role="checkbox" data-ph-at-id="save-click" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LoOray" class="au-target" au-target-id="308" id="save-653651-13" aria-label="Save Senior Software Engineer job ID 653651 to job cart" aria-checked="false">
#                                                                             <span class="label-content" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5iZTnr">
#                                                                                 <i class="icon icon-star-empty" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-3hSiPg"></i>
#                                                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSaveText" data-ph-at-id="save-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-V3uiSa">
#                 Save
#                </ppc-content>
#                                                                             </span><!--anchor-->
#                                                                             <!--anchor-->
#                                                                         </label>
#                                                                     </div><!--anchor-->
#                                                                 </div>
#                                                                  <!--End Job saved block -->
#                                                             </div>
#                                                         </div>
#                                                     </li><li class="jobs-list-item" data-ph-at-id="jobs-list-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-y4hTr0">
#                                                         <div class="information-block row" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-zEw2pE">
#                                                             <div class="left-block col-xs-12 col-md-10" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-rmeHWW">
#                                                                 <!-- jobs link block -->
#                                                                 <div class="information" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-fm9Dgs">
#                                                                     <a focus.bind="$index == 0 &amp;&amp; currentSelectedPage > 1" ph-tevent="job_click" ref="linkEle" role="link" key-role="2fssdu-ph-search-results-v1-view-external-linkRole" target="_blank" data-ph-at-id="job-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ic7VNu" class="au-target" au-target-id="288" ph-click-ctx="job" ph-tref="1569669868437155a7" ph-tag="ph-search-results-v1" href="https://careers.microsoft.com/us/en/job/389313/Support-Escal-Eng-ARR" aria-label="Support Escal Eng_ARR job ID 389313 opens in a new tab" data-ph-at-job-title-text="Support Escal Eng_ARR" data-ph-at-job-location-text="Shanghai, Shanghai, China" data-ph-at-job-category-text="Services" data-ph-at-job-id-text="389313" data-ph-at-job-type-text="" data-ph-at-job-industry-text="" data-ph-at-job-post-date-text="2018-04-11T23:30:00" data-ph-at-job-seqno-text="389313" data-ph-at-job-position-text="" data-ph-at-job-employment-type-text="" data-ph-at-job-role-type-text="" data-ph-at-job-education-level-text="">
#                                                                         <span class="job-title" data-ph-at-id="searchresults-job-title" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-MRnq6A">Support Escal Eng_ARR</span>
#                                                                     </a>
#                                                                     <div class="job-additional-info" data-ph-at-id="job-info" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LesJKv">
#                                                                         <span class="job-location" data-ph-at-id="searchresults-job-location" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CQMOUl">
#                                                                             Shanghai, Shanghai, China
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-category" data-ph-at-id="searchresults-job-category" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-g94YTa">
#                                                                             Services
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-date au-target" data-ph-at-id="searchresults-job-postdate" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-b6UGw3" au-target-id="294" aria-label="Apr 11th 2018">
#                                                                             Apr 11, 2018
#                                                                         </span><!--anchor-->
#                                                                     </div>
#                                                                     <div class="description au-target" innerhtml.bind="eachResult.descriptionTeaser | sanitizeHTML" data-ph-at-id="jobdescription-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Abw08f" au-target-id="297">As cloud goes main stream, Azure leads the way. Azure’s continued success depends on providing customers a world class support experience. Love services, support in the cloud? Customer obsessed?</div>
#                                                                 </div>
#                                                                 <!--End jobs link block -->
#
#                                                                 <!-- jobs multilocation block -->
#                                                                 <!--anchor-->
#                                                                 <!--End jobs multilocation block -->
#                                                             </div>
#                                                             <div class="right-block col-xs-12 col-md-2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-W9vvx1">
#                                                                 <!-- Job applied status block -->
#                                                                 <div class="applied-action" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0WA3mP">
#                                                                     <section class="ph-widget" instance-id="we3alx" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CGkAfP" view="1565777110184-default" original-view="default" theme="default">
#                                                                         <div as-element="ph-job-status-v1" arrjoblist.bind="$index===0 ? jobResults : null" jobid="${eachResult.jobSeqNo}" view="1565777110184-default" mode="APPLY" class="ph-job-status-v1-default-default ph-widget-target au-target" data-widget="ph-job-status-v1" instance-id="we3alx" original-view="default" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TWsAYD" au-target-id="306">
#
#                                                                             <!--anchor-->
#                                                                         <!--anchor--></div>
#                                                                     </section>
#                                                                 </div>
#                                                                 <!--End Job applied status block -->
#
#                                                                 <!-- Job saved block -->
#                                                                 <div class="actions" data-ph-at-id="job-actions" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Kt42DX">
#                                                                     <!--<div as-element="ph-add-to-cart-v1" if.bind="!bulkcart" data-widget="ph-add-to-cart-v1" job-detail.bind="eachResult" class="ph-add-to-cart-v1-default-default" view="view1"></div>-->
#                                                                     <div class="savejob-checkbox" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-lWmxkg">
#                                                                         <label data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-eySiqX" class="au-target" au-target-id="307" for="save-389313-14">
#                                                                             <input type="checkbox" checked.bind="eachResult.isJobSaved" change.delegate="handleSaveJob(eachResult)" role="checkbox" data-ph-at-id="save-click" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LoOray" class="au-target" au-target-id="308" id="save-389313-14" aria-label="Save Support Escal Eng_ARR job ID 389313 to job cart" aria-checked="false">
#                                                                             <span class="label-content" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5iZTnr">
#                                                                                 <i class="icon icon-star-empty" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-3hSiPg"></i>
#                                                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSaveText" data-ph-at-id="save-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-V3uiSa">
#                 Save
#                </ppc-content>
#                                                                             </span><!--anchor-->
#                                                                             <!--anchor-->
#                                                                         </label>
#                                                                     </div><!--anchor-->
#                                                                 </div>
#                                                                  <!--End Job saved block -->
#                                                             </div>
#                                                         </div>
#                                                     </li><li class="jobs-list-item" data-ph-at-id="jobs-list-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-y4hTr0">
#                                                         <div class="information-block row" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-zEw2pE">
#                                                             <div class="left-block col-xs-12 col-md-10" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-rmeHWW">
#                                                                 <!-- jobs link block -->
#                                                                 <div class="information" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-fm9Dgs">
#                                                                     <a focus.bind="$index == 0 &amp;&amp; currentSelectedPage > 1" ph-tevent="job_click" ref="linkEle" role="link" key-role="2fssdu-ph-search-results-v1-view-external-linkRole" target="_blank" data-ph-at-id="job-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ic7VNu" class="au-target" au-target-id="288" ph-click-ctx="job" ph-tref="15696698684371c110" ph-tag="ph-search-results-v1" href="https://careers.microsoft.com/us/en/job/703831/Support-Escalation-Engineer-Azure-App-Services" aria-label="Support Escalation Engineer Azure App Services job ID 703831 opens in a new tab" data-ph-at-job-title-text="Support Escalation Engineer Azure App Services" data-ph-at-job-location-text="Bucharest, Bucharest, Romania" data-ph-at-job-category-text="Services" data-ph-at-job-id-text="703831" data-ph-at-job-type-text="" data-ph-at-job-industry-text="" data-ph-at-job-post-date-text="2019-09-13T08:40:00" data-ph-at-job-seqno-text="703831" data-ph-at-job-position-text="" data-ph-at-job-employment-type-text="" data-ph-at-job-role-type-text="" data-ph-at-job-education-level-text="">
#                                                                         <span class="job-title" data-ph-at-id="searchresults-job-title" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-MRnq6A">Support Escalation Engineer Azure App Services</span>
#                                                                     </a>
#                                                                     <div class="job-additional-info" data-ph-at-id="job-info" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LesJKv">
#                                                                         <!--anchor-->
#                                                                         <span class="job-category" data-ph-at-id="searchresults-job-category" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-g94YTa">
#                                                                             Services
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-date au-target" data-ph-at-id="searchresults-job-postdate" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-b6UGw3" au-target-id="294" aria-label="Sep 13th 2019">
#                                                                             Sep 13, 2019
#                                                                         </span><!--anchor-->
#                                                                     </div>
#                                                                     <div class="description au-target" innerhtml.bind="eachResult.descriptionTeaser | sanitizeHTML" data-ph-at-id="jobdescription-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Abw08f" au-target-id="297">The Azure Engineer is a trusted advisor to fellow IT Professionals, using broad and in-depth troubleshooting skills and product knowledge to solve challenging technical problems. Frequently, these</div>
#                                                                 </div>
#                                                                 <!--End jobs link block -->
#
#                                                                 <!-- jobs multilocation block -->
#                                                                 <div class="job-multi-locations" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-vJOVzG">
#                                                                     <button ph-tevent="multi_location_click" keyup.trigger="($event.keyCode === 27)?(eachResult.toggleOpen = false):''" class="esc$$close au-target" click.delegate="eachResult.toggleOpen = !eachResult.toggleOpen" role="button" key-role="IWwth6-2fssdu-ph-search-results-v1-view-external-btnRole" data-ph-at-id="job-multi-locations-button" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0aUp1e" au-target-id="298" data-ph-tevent-attr-trait14="Services" data-ph-tevent-attr-trait5="703831" id="searchLoc-15" aria-expanded="false" aria-label="Support Escalation Engineer Azure App Services job ID 703831 Job available in 2 locations" data-ph-at-job-multilocation-count="2">
#                                                                         <span data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-h6pjaT"><ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultJobAvailText1" data-ph-at-id="multilocation-text1" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5DjjWH">
#               Job available in
#              </ppc-content></span> 2 <span data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5Lm1HA"><ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultJobAvailText2" data-ph-at-id="multilocation-text2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-2Go8OT">
#               locations
#              </ppc-content></span>
#                                                                         <!--icon toggle based on item click: js dependent-->
#                                                                         <!--<i ref="listItemIcon" class="icon icon-down-arrow" aria-hidden="true"></i>-->
#                                                                         <i ref="listItemIcon" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-KotPHt" class="au-target icon icon-down-arrow" au-target-id="300"></i>
#                                                                     </button>
#                                                                     <!--dropView used to toggle toggleMultiLocationView based on item click: js dependent-->
#                                                                     <ul ref="listItem" data-ph-at-id="job-multi-locations-list" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-cbms8u" class="au-target hide" au-target-id="301" aria-hidden="true">
#                                                                         <li class="location au-target" data-ph-at-id="job-multi-location-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-EgsS0Q" au-target-id="302" aria-label="Bucharest, Bucharest, Romania" data-ph-at-job-location-text="Bucharest, Bucharest, Romania">
#                                                                             Bucharest, Bucharest, Romania
#                                                                         </li><li class="location au-target" data-ph-at-id="job-multi-location-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-EgsS0Q" au-target-id="302" aria-label="Timisoara, Timis, Romania" data-ph-at-job-location-text="Timisoara, Timis, Romania">
#                                                                             Timisoara, Timis, Romania
#                                                                         </li><!--anchor-->
#                                                                     </ul>
#                                                                 </div><!--anchor-->
#                                                                 <!--End jobs multilocation block -->
#                                                             </div>
#                                                             <div class="right-block col-xs-12 col-md-2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-W9vvx1">
#                                                                 <!-- Job applied status block -->
#                                                                 <div class="applied-action" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0WA3mP">
#                                                                     <section class="ph-widget" instance-id="we3alx" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CGkAfP" view="1565777110184-default" original-view="default" theme="default">
#                                                                         <div as-element="ph-job-status-v1" arrjoblist.bind="$index===0 ? jobResults : null" jobid="${eachResult.jobSeqNo}" view="1565777110184-default" mode="APPLY" class="ph-job-status-v1-default-default ph-widget-target au-target" data-widget="ph-job-status-v1" instance-id="we3alx" original-view="default" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TWsAYD" au-target-id="306">
#
#                                                                             <!--anchor-->
#                                                                         <!--anchor--></div>
#                                                                     </section>
#                                                                 </div>
#                                                                 <!--End Job applied status block -->
#
#                                                                 <!-- Job saved block -->
#                                                                 <div class="actions" data-ph-at-id="job-actions" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Kt42DX">
#                                                                     <!--<div as-element="ph-add-to-cart-v1" if.bind="!bulkcart" data-widget="ph-add-to-cart-v1" job-detail.bind="eachResult" class="ph-add-to-cart-v1-default-default" view="view1"></div>-->
#                                                                     <div class="savejob-checkbox" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-lWmxkg">
#                                                                         <label data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-eySiqX" class="au-target" au-target-id="307" for="save-703831-15">
#                                                                             <input type="checkbox" checked.bind="eachResult.isJobSaved" change.delegate="handleSaveJob(eachResult)" role="checkbox" data-ph-at-id="save-click" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LoOray" class="au-target" au-target-id="308" id="save-703831-15" aria-label="Save Support Escalation Engineer Azure App Services job ID 703831 to job cart" aria-checked="false">
#                                                                             <span class="label-content" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5iZTnr">
#                                                                                 <i class="icon icon-star-empty" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-3hSiPg"></i>
#                                                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSaveText" data-ph-at-id="save-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-V3uiSa">
#                 Save
#                </ppc-content>
#                                                                             </span><!--anchor-->
#                                                                             <!--anchor-->
#                                                                         </label>
#                                                                     </div><!--anchor-->
#                                                                 </div>
#                                                                  <!--End Job saved block -->
#                                                             </div>
#                                                         </div>
#                                                     </li><li class="jobs-list-item" data-ph-at-id="jobs-list-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-y4hTr0">
#                                                         <div class="information-block row" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-zEw2pE">
#                                                             <div class="left-block col-xs-12 col-md-10" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-rmeHWW">
#                                                                 <!-- jobs link block -->
#                                                                 <div class="information" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-fm9Dgs">
#                                                                     <a focus.bind="$index == 0 &amp;&amp; currentSelectedPage > 1" ph-tevent="job_click" ref="linkEle" role="link" key-role="2fssdu-ph-search-results-v1-view-external-linkRole" target="_blank" data-ph-at-id="job-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ic7VNu" class="au-target" au-target-id="288" ph-click-ctx="job" ph-tref="15696698684381a59d" ph-tag="ph-search-results-v1" href="https://careers.microsoft.com/us/en/job/704768/Support-Escalation-Engineer" aria-label="Support Escalation Engineer job ID 704768 opens in a new tab" data-ph-at-job-title-text="Support Escalation Engineer" data-ph-at-job-location-text="Hyderabad, Telangana, India" data-ph-at-job-category-text="Services" data-ph-at-job-id-text="704768" data-ph-at-job-type-text="" data-ph-at-job-industry-text="" data-ph-at-job-post-date-text="2019-09-19T12:05:00" data-ph-at-job-seqno-text="704768" data-ph-at-job-position-text="" data-ph-at-job-employment-type-text="" data-ph-at-job-role-type-text="" data-ph-at-job-education-level-text="">
#                                                                         <span class="job-title" data-ph-at-id="searchresults-job-title" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-MRnq6A">Support Escalation Engineer</span>
#                                                                     </a>
#                                                                     <div class="job-additional-info" data-ph-at-id="job-info" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LesJKv">
#                                                                         <span class="job-location" data-ph-at-id="searchresults-job-location" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CQMOUl">
#                                                                             Hyderabad, Telangana, India
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-category" data-ph-at-id="searchresults-job-category" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-g94YTa">
#                                                                             Services
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-date au-target" data-ph-at-id="searchresults-job-postdate" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-b6UGw3" au-target-id="294" aria-label="Sep 19th 2019">
#                                                                             Sep 19, 2019
#                                                                         </span><!--anchor-->
#                                                                     </div>
#                                                                     <div class="description au-target" innerhtml.bind="eachResult.descriptionTeaser | sanitizeHTML" data-ph-at-id="jobdescription-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Abw08f" au-target-id="297">• As cloud goes main stream, Azure leads the way. Azure's continued success depends on providing customers a world class support experience. Love services, support in the cloud? Customer</div>
#                                                                 </div>
#                                                                 <!--End jobs link block -->
#
#                                                                 <!-- jobs multilocation block -->
#                                                                 <!--anchor-->
#                                                                 <!--End jobs multilocation block -->
#                                                             </div>
#                                                             <div class="right-block col-xs-12 col-md-2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-W9vvx1">
#                                                                 <!-- Job applied status block -->
#                                                                 <div class="applied-action" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0WA3mP">
#                                                                     <section class="ph-widget" instance-id="we3alx" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CGkAfP" view="1565777110184-default" original-view="default" theme="default">
#                                                                         <div as-element="ph-job-status-v1" arrjoblist.bind="$index===0 ? jobResults : null" jobid="${eachResult.jobSeqNo}" view="1565777110184-default" mode="APPLY" class="ph-job-status-v1-default-default ph-widget-target au-target" data-widget="ph-job-status-v1" instance-id="we3alx" original-view="default" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TWsAYD" au-target-id="306">
#
#                                                                             <!--anchor-->
#                                                                         <!--anchor--></div>
#                                                                     </section>
#                                                                 </div>
#                                                                 <!--End Job applied status block -->
#
#                                                                 <!-- Job saved block -->
#                                                                 <div class="actions" data-ph-at-id="job-actions" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Kt42DX">
#                                                                     <!--<div as-element="ph-add-to-cart-v1" if.bind="!bulkcart" data-widget="ph-add-to-cart-v1" job-detail.bind="eachResult" class="ph-add-to-cart-v1-default-default" view="view1"></div>-->
#                                                                     <div class="savejob-checkbox" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-lWmxkg">
#                                                                         <label data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-eySiqX" class="au-target" au-target-id="307" for="save-704768-16">
#                                                                             <input type="checkbox" checked.bind="eachResult.isJobSaved" change.delegate="handleSaveJob(eachResult)" role="checkbox" data-ph-at-id="save-click" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LoOray" class="au-target" au-target-id="308" id="save-704768-16" aria-label="Save Support Escalation Engineer job ID 704768 to job cart" aria-checked="false">
#                                                                             <span class="label-content" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5iZTnr">
#                                                                                 <i class="icon icon-star-empty" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-3hSiPg"></i>
#                                                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSaveText" data-ph-at-id="save-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-V3uiSa">
#                 Save
#                </ppc-content>
#                                                                             </span><!--anchor-->
#                                                                             <!--anchor-->
#                                                                         </label>
#                                                                     </div><!--anchor-->
#                                                                 </div>
#                                                                  <!--End Job saved block -->
#                                                             </div>
#                                                         </div>
#                                                     </li><li class="jobs-list-item" data-ph-at-id="jobs-list-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-y4hTr0">
#                                                         <div class="information-block row" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-zEw2pE">
#                                                             <div class="left-block col-xs-12 col-md-10" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-rmeHWW">
#                                                                 <!-- jobs link block -->
#                                                                 <div class="information" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-fm9Dgs">
#                                                                     <a focus.bind="$index == 0 &amp;&amp; currentSelectedPage > 1" ph-tevent="job_click" ref="linkEle" role="link" key-role="2fssdu-ph-search-results-v1-view-external-linkRole" target="_blank" data-ph-at-id="job-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ic7VNu" class="au-target" au-target-id="288" ph-click-ctx="job" ph-tref="15696698684391be06" ph-tag="ph-search-results-v1" href="https://careers.microsoft.com/us/en/job/654470/Software-Engineer-II" aria-label="Software Engineer II job ID 654470 opens in a new tab" data-ph-at-job-title-text="Software Engineer II" data-ph-at-job-location-text="Redmond, Washington, United States" data-ph-at-job-category-text="Engineering" data-ph-at-job-id-text="654470" data-ph-at-job-type-text="" data-ph-at-job-industry-text="" data-ph-at-job-post-date-text="2019-06-28T19:24:00" data-ph-at-job-seqno-text="654470" data-ph-at-job-position-text="" data-ph-at-job-employment-type-text="" data-ph-at-job-role-type-text="" data-ph-at-job-education-level-text="">
#                                                                         <span class="job-title" data-ph-at-id="searchresults-job-title" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-MRnq6A">Software Engineer II</span>
#                                                                     </a>
#                                                                     <div class="job-additional-info" data-ph-at-id="job-info" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LesJKv">
#                                                                         <span class="job-location" data-ph-at-id="searchresults-job-location" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CQMOUl">
#                                                                             Redmond, Washington, United States
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-category" data-ph-at-id="searchresults-job-category" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-g94YTa">
#                                                                             Engineering
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-date au-target" data-ph-at-id="searchresults-job-postdate" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-b6UGw3" au-target-id="294" aria-label="Jun 28th 2019">
#                                                                             Jun 28, 2019
#                                                                         </span><!--anchor-->
#                                                                     </div>
#                                                                     <div class="description au-target" innerhtml.bind="eachResult.descriptionTeaser | sanitizeHTML" data-ph-at-id="jobdescription-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Abw08f" au-target-id="297">The Linux Systems Group is looking for a talented Software Engineer to join our team. If you are interested in working on Linux or open source technologies at Microsoft, this is the right team for</div>
#                                                                 </div>
#                                                                 <!--End jobs link block -->
#
#                                                                 <!-- jobs multilocation block -->
#                                                                 <!--anchor-->
#                                                                 <!--End jobs multilocation block -->
#                                                             </div>
#                                                             <div class="right-block col-xs-12 col-md-2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-W9vvx1">
#                                                                 <!-- Job applied status block -->
#                                                                 <div class="applied-action" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0WA3mP">
#                                                                     <section class="ph-widget" instance-id="we3alx" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CGkAfP" view="1565777110184-default" original-view="default" theme="default">
#                                                                         <div as-element="ph-job-status-v1" arrjoblist.bind="$index===0 ? jobResults : null" jobid="${eachResult.jobSeqNo}" view="1565777110184-default" mode="APPLY" class="ph-job-status-v1-default-default ph-widget-target au-target" data-widget="ph-job-status-v1" instance-id="we3alx" original-view="default" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TWsAYD" au-target-id="306">
#
#                                                                             <!--anchor-->
#                                                                         <!--anchor--></div>
#                                                                     </section>
#                                                                 </div>
#                                                                 <!--End Job applied status block -->
#
#                                                                 <!-- Job saved block -->
#                                                                 <div class="actions" data-ph-at-id="job-actions" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Kt42DX">
#                                                                     <!--<div as-element="ph-add-to-cart-v1" if.bind="!bulkcart" data-widget="ph-add-to-cart-v1" job-detail.bind="eachResult" class="ph-add-to-cart-v1-default-default" view="view1"></div>-->
#                                                                     <div class="savejob-checkbox" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-lWmxkg">
#                                                                         <label data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-eySiqX" class="au-target" au-target-id="307" for="save-654470-17">
#                                                                             <input type="checkbox" checked.bind="eachResult.isJobSaved" change.delegate="handleSaveJob(eachResult)" role="checkbox" data-ph-at-id="save-click" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LoOray" class="au-target" au-target-id="308" id="save-654470-17" aria-label="Save Software Engineer II job ID 654470 to job cart" aria-checked="false">
#                                                                             <span class="label-content" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5iZTnr">
#                                                                                 <i class="icon icon-star-empty" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-3hSiPg"></i>
#                                                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSaveText" data-ph-at-id="save-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-V3uiSa">
#                 Save
#                </ppc-content>
#                                                                             </span><!--anchor-->
#                                                                             <!--anchor-->
#                                                                         </label>
#                                                                     </div><!--anchor-->
#                                                                 </div>
#                                                                  <!--End Job saved block -->
#                                                             </div>
#                                                         </div>
#                                                     </li><li class="jobs-list-item" data-ph-at-id="jobs-list-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-y4hTr0">
#                                                         <div class="information-block row" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-zEw2pE">
#                                                             <div class="left-block col-xs-12 col-md-10" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-rmeHWW">
#                                                                 <!-- jobs link block -->
#                                                                 <div class="information" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-fm9Dgs">
#                                                                     <a focus.bind="$index == 0 &amp;&amp; currentSelectedPage > 1" ph-tevent="job_click" ref="linkEle" role="link" key-role="2fssdu-ph-search-results-v1-view-external-linkRole" target="_blank" data-ph-at-id="job-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ic7VNu" class="au-target" au-target-id="288" ph-click-ctx="job" ph-tref="156966986843910910" ph-tag="ph-search-results-v1" href="https://careers.microsoft.com/us/en/job/662515/Support-Escalation-Engineer-Azure-Rapid-Response" aria-label="Support Escalation Engineer_Azure Rapid Response job ID 662515 opens in a new tab" data-ph-at-job-title-text="Support Escalation Engineer_Azure Rapid Response" data-ph-at-job-location-text="Taipei, Taipei City, Taiwan" data-ph-at-job-category-text="Services" data-ph-at-job-id-text="662515" data-ph-at-job-type-text="" data-ph-at-job-industry-text="" data-ph-at-job-post-date-text="2019-09-16T02:30:00" data-ph-at-job-seqno-text="662515" data-ph-at-job-position-text="" data-ph-at-job-employment-type-text="" data-ph-at-job-role-type-text="" data-ph-at-job-education-level-text="">
#                                                                         <span class="job-title" data-ph-at-id="searchresults-job-title" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-MRnq6A">Support Escalation Engineer_Azure Rapid Response</span>
#                                                                     </a>
#                                                                     <div class="job-additional-info" data-ph-at-id="job-info" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LesJKv">
#                                                                         <span class="job-location" data-ph-at-id="searchresults-job-location" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CQMOUl">
#                                                                             Taipei, Taipei City, Taiwan
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-category" data-ph-at-id="searchresults-job-category" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-g94YTa">
#                                                                             Services
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-date au-target" data-ph-at-id="searchresults-job-postdate" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-b6UGw3" au-target-id="294" aria-label="Sep 16th 2019">
#                                                                             Sep 16, 2019
#                                                                         </span><!--anchor-->
#                                                                     </div>
#                                                                     <div class="description au-target" innerhtml.bind="eachResult.descriptionTeaser | sanitizeHTML" data-ph-at-id="jobdescription-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Abw08f" au-target-id="297">As cloud goes main stream, Azure leads the way. Azure's continued success depends on providing customers a world class support experience. Love services, support in the cloud? Customer obsessed? Data</div>
#                                                                 </div>
#                                                                 <!--End jobs link block -->
#
#                                                                 <!-- jobs multilocation block -->
#                                                                 <!--anchor-->
#                                                                 <!--End jobs multilocation block -->
#                                                             </div>
#                                                             <div class="right-block col-xs-12 col-md-2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-W9vvx1">
#                                                                 <!-- Job applied status block -->
#                                                                 <div class="applied-action" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0WA3mP">
#                                                                     <section class="ph-widget" instance-id="we3alx" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CGkAfP" view="1565777110184-default" original-view="default" theme="default">
#                                                                         <div as-element="ph-job-status-v1" arrjoblist.bind="$index===0 ? jobResults : null" jobid="${eachResult.jobSeqNo}" view="1565777110184-default" mode="APPLY" class="ph-job-status-v1-default-default ph-widget-target au-target" data-widget="ph-job-status-v1" instance-id="we3alx" original-view="default" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TWsAYD" au-target-id="306">
#
#                                                                             <!--anchor-->
#                                                                         <!--anchor--></div>
#                                                                     </section>
#                                                                 </div>
#                                                                 <!--End Job applied status block -->
#
#                                                                 <!-- Job saved block -->
#                                                                 <div class="actions" data-ph-at-id="job-actions" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Kt42DX">
#                                                                     <!--<div as-element="ph-add-to-cart-v1" if.bind="!bulkcart" data-widget="ph-add-to-cart-v1" job-detail.bind="eachResult" class="ph-add-to-cart-v1-default-default" view="view1"></div>-->
#                                                                     <div class="savejob-checkbox" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-lWmxkg">
#                                                                         <label data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-eySiqX" class="au-target" au-target-id="307" for="save-662515-18">
#                                                                             <input type="checkbox" checked.bind="eachResult.isJobSaved" change.delegate="handleSaveJob(eachResult)" role="checkbox" data-ph-at-id="save-click" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LoOray" class="au-target" au-target-id="308" id="save-662515-18" aria-label="Save Support Escalation Engineer_Azure Rapid Response job ID 662515 to job cart" aria-checked="false">
#                                                                             <span class="label-content" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5iZTnr">
#                                                                                 <i class="icon icon-star-empty" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-3hSiPg"></i>
#                                                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSaveText" data-ph-at-id="save-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-V3uiSa">
#                 Save
#                </ppc-content>
#                                                                             </span><!--anchor-->
#                                                                             <!--anchor-->
#                                                                         </label>
#                                                                     </div><!--anchor-->
#                                                                 </div>
#                                                                  <!--End Job saved block -->
#                                                             </div>
#                                                         </div>
#                                                     </li><li class="jobs-list-item" data-ph-at-id="jobs-list-item" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-y4hTr0">
#                                                         <div class="information-block row" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-zEw2pE">
#                                                             <div class="left-block col-xs-12 col-md-10" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-rmeHWW">
#                                                                 <!-- jobs link block -->
#                                                                 <div class="information" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-fm9Dgs">
#                                                                     <a focus.bind="$index == 0 &amp;&amp; currentSelectedPage > 1" ph-tevent="job_click" ref="linkEle" role="link" key-role="2fssdu-ph-search-results-v1-view-external-linkRole" target="_blank" data-ph-at-id="job-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ic7VNu" class="au-target" au-target-id="288" ph-click-ctx="job" ph-tref="15696698684401bc6d" ph-tag="ph-search-results-v1" href="https://careers.microsoft.com/us/en/job/648261/Support-Engineer-Azure-App-Services" aria-label="Support Engineer - Azure App Services job ID 648261 opens in a new tab" data-ph-at-job-title-text="Support Engineer - Azure App Services" data-ph-at-job-location-text="Amman, Amman, Jordan" data-ph-at-job-category-text="Services" data-ph-at-job-id-text="648261" data-ph-at-job-type-text="" data-ph-at-job-industry-text="" data-ph-at-job-post-date-text="2019-09-16T09:03:00" data-ph-at-job-seqno-text="648261" data-ph-at-job-position-text="" data-ph-at-job-employment-type-text="" data-ph-at-job-role-type-text="" data-ph-at-job-education-level-text="">
#                                                                         <span class="job-title" data-ph-at-id="searchresults-job-title" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-MRnq6A">Support Engineer - Azure App Services</span>
#                                                                     </a>
#                                                                     <div class="job-additional-info" data-ph-at-id="job-info" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LesJKv">
#                                                                         <span class="job-location" data-ph-at-id="searchresults-job-location" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CQMOUl">
#                                                                             Amman, Amman, Jordan
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-category" data-ph-at-id="searchresults-job-category" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-g94YTa">
#                                                                             Services
#                                                                         </span><!--anchor-->
#                                                                         <span class="job-date au-target" data-ph-at-id="searchresults-job-postdate" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-b6UGw3" au-target-id="294" aria-label="Sep 16th 2019">
#                                                                             Sep 16, 2019
#                                                                         </span><!--anchor-->
#                                                                     </div>
#                                                                     <div class="description au-target" innerhtml.bind="eachResult.descriptionTeaser | sanitizeHTML" data-ph-at-id="jobdescription-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Abw08f" au-target-id="297"> The CSS (Customer Service and Support), provides high technical service and 3rd and 4th level support for Microsoft’s Global Enterprise and Development customers.Since the CSS (Customer Service</div>
#                                                                 </div>
#                                                                 <!--End jobs link block -->
#
#                                                                 <!-- jobs multilocation block -->
#                                                                 <!--anchor-->
#                                                                 <!--End jobs multilocation block -->
#                                                             </div>
#                                                             <div class="right-block col-xs-12 col-md-2" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-W9vvx1">
#                                                                 <!-- Job applied status block -->
#                                                                 <div class="applied-action" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-0WA3mP">
#                                                                     <section class="ph-widget" instance-id="we3alx" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-CGkAfP" view="1565777110184-default" original-view="default" theme="default">
#                                                                         <div as-element="ph-job-status-v1" arrjoblist.bind="$index===0 ? jobResults : null" jobid="${eachResult.jobSeqNo}" view="1565777110184-default" mode="APPLY" class="ph-job-status-v1-default-default ph-widget-target au-target" data-widget="ph-job-status-v1" instance-id="we3alx" original-view="default" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TWsAYD" au-target-id="306">
#
#                                                                             <!--anchor-->
#                                                                         <!--anchor--></div>
#                                                                     </section>
#                                                                 </div>
#                                                                 <!--End Job applied status block -->
#
#                                                                 <!-- Job saved block -->
#                                                                 <div class="actions" data-ph-at-id="job-actions" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Kt42DX">
#                                                                     <!--<div as-element="ph-add-to-cart-v1" if.bind="!bulkcart" data-widget="ph-add-to-cart-v1" job-detail.bind="eachResult" class="ph-add-to-cart-v1-default-default" view="view1"></div>-->
#                                                                     <div class="savejob-checkbox" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-lWmxkg">
#                                                                         <label data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-eySiqX" class="au-target" au-target-id="307" for="save-648261-19">
#                                                                             <input type="checkbox" checked.bind="eachResult.isJobSaved" change.delegate="handleSaveJob(eachResult)" role="checkbox" data-ph-at-id="save-click" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-LoOray" class="au-target" au-target-id="308" id="save-648261-19" aria-label="Save Support Engineer - Azure App Services job ID 648261 to job cart" aria-checked="false">
#                                                                             <span class="label-content" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-5iZTnr">
#                                                                                 <i class="icon icon-star-empty" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-3hSiPg"></i>
#                                                                                 <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultSaveText" data-ph-at-id="save-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-V3uiSa">
#                 Save
#                </ppc-content>
#                                                                             </span><!--anchor-->
#                                                                             <!--anchor-->
#                                                                         </label>
#                                                                     </div><!--anchor-->
#                                                                 </div>
#                                                                  <!--End Job saved block -->
#                                                             </div>
#                                                         </div>
#                                                     </li><!--anchor-->
#                                                 </ul>
#                                             </div>
#                                         </div>
#                                         <!--End Facet results-->
#                                         <!--Bottom Result count block -->
#                                         <div class="pagination-block au-target" show.bind="paginationRange.length > 1" data-ph-at-id="pagination-block" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-NqUtB4" au-target-id="313">
#                                             <div class="search-bottom-count au-target" data-ph-at-id="pagination-info" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-WzXjXE" au-target-id="314" data-ph-at-starting-job-number-text="1" data-ph-at-ending-job-number-text="20" data-ph-at-total-jobs-text="107">
#                                                 <span data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-A0f9qa">
#                                                     <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultPaginationText" data-ph-at-id="showing-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-7ZTFG1"> Showing </ppc-content>
#                                                     <span class="job-number" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-v3eF8w"> 1 </span>
#                                                     <span class="job-number" aria-hidden="true" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Ks6MAG">
#                                                         <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResulttPaginationHyphenText" data-ph-at-id="hyphen-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-rgOn5T"> - </ppc-content>
#                                                     </span>
#                                                     <span class="sr-only" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-H5FW4P"><ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResulttPaginationToText" data-ph-at-id="to-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-hX5Etf">to</ppc-content></span>
#                                                     <span class="job-number" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-wRvYTe"> 20 </span>
#                                                     <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResulttPaginationOfText" data-ph-at-id="of-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-y4CzyC"> of</ppc-content>
#                                                 </span><!--anchor-->
#                                                 <span class="total-jobs" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-k8yAFK"> 107 </span>
#                                                 <!--anchor-->
#                                                 <span data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-R5DwsU">
#                                                     <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResulttPaginationResText" data-ph-at-id="results-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-NPnFds">results</ppc-content>
#                                                 </span><!--anchor-->
#                                                 <span data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-lbxlHZ">
#                                                     <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResulttPaginationForText" data-ph-at-id="for-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-6xu68J">for</ppc-content>
#                                                 </span><!--anchor-->
#                                                 <span class="search-keyword" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-HxZYsR">php</span><!--anchor-->
#                                                 <!--anchor-->
#                                             </div>
#                                             <!--End Bottom Result count block -->
#
#                                             <!-- Bottom Pagination block -->
#                                             <div role="region" aria-label="pagination block" key-aria-label="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultPaginationBlockAriaLabelText" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-MgIi4Z">
#                                                 <ul class="pagination" data-ph-at-id="pagination" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-eaRwzq">
#                                                     <li data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-NzMW9r">
#                                                         <a href.bind="paginationUrl(currentSelectedPage - 1)" aria-label="View previous page" key-aria-label="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultBottomPrevAriaLabelText" show.bind="prevButtonVisibility" ph-tevent="pagination_click" data-ph-tevent-attr-trait214="Previous" role="button" key-role="Ufch4m-2fssdu-ph-search-results-v1-view-external-btnRole" data-ph-at-id="pagination-previous-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-tb6U4s" class="au-target aurelia-hide" au-target-id="326" href="https://careers.microsoft.com/us/en/search-results?keywords=php&amp;s=1">
#                                                             <ppc-content type="icon" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-wmx9c7">
#                                                                 <span aria-hidden="true" class="icon icon-left-arrow" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-YGmDzY"></span>
#                                                             </ppc-content>
#                                                             <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultBottomPrevText" data-ph-at-id="pagination-previous-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-aTG1pH">
#            Prev
#          </ppc-content>
#                                                         </a>
#                                                     </li>
#                                                     <li data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TTJEHU" class="au-target active" au-target-id="327">
#                                                         <a href.bind="paginationUrl(page)" onclick="getElementById('eachJob').focus()" ph-tevent="pagination_click" role="button" key-aria-label="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultPaginationDynamicAriaLabelText" data-ph-at-id="pagination-page-number-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ms3YtQ" class="au-target" au-target-id="328" href="https://careers.microsoft.com/us/en/search-results?keywords=php&amp;s=1" data-ph-tevent-attr-trait214="1" aria-label="current page 1" data-ph-at-text="1">1</a>
#                                                     </li><li data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TTJEHU" class="au-target" au-target-id="327">
#                                                         <a href.bind="paginationUrl(page)" onclick="getElementById('eachJob').focus()" ph-tevent="pagination_click" role="button" key-aria-label="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultPaginationDynamicAriaLabelText" data-ph-at-id="pagination-page-number-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ms3YtQ" class="au-target" au-target-id="328" href="https://careers.microsoft.com/us/en/search-results?keywords=php&amp;from=20&amp;s=1" data-ph-tevent-attr-trait214="2" aria-label="page 2" data-ph-at-text="2">2</a>
#                                                     </li><li data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TTJEHU" class="au-target" au-target-id="327">
#                                                         <a href.bind="paginationUrl(page)" onclick="getElementById('eachJob').focus()" ph-tevent="pagination_click" role="button" key-aria-label="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultPaginationDynamicAriaLabelText" data-ph-at-id="pagination-page-number-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ms3YtQ" class="au-target" au-target-id="328" href="https://careers.microsoft.com/us/en/search-results?keywords=php&amp;from=40&amp;s=1" data-ph-tevent-attr-trait214="3" aria-label="page 3" data-ph-at-text="3">3</a>
#                                                     </li><li data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TTJEHU" class="au-target" au-target-id="327">
#                                                         <a href.bind="paginationUrl(page)" onclick="getElementById('eachJob').focus()" ph-tevent="pagination_click" role="button" key-aria-label="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultPaginationDynamicAriaLabelText" data-ph-at-id="pagination-page-number-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ms3YtQ" class="au-target" au-target-id="328" href="https://careers.microsoft.com/us/en/search-results?keywords=php&amp;from=60&amp;s=1" data-ph-tevent-attr-trait214="4" aria-label="page 4" data-ph-at-text="4">4</a>
#                                                     </li><li data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TTJEHU" class="au-target" au-target-id="327">
#                                                         <a href.bind="paginationUrl(page)" onclick="getElementById('eachJob').focus()" ph-tevent="pagination_click" role="button" key-aria-label="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultPaginationDynamicAriaLabelText" data-ph-at-id="pagination-page-number-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ms3YtQ" class="au-target" au-target-id="328" href="https://careers.microsoft.com/us/en/search-results?keywords=php&amp;from=80&amp;s=1" data-ph-tevent-attr-trait214="5" aria-label="page 5" data-ph-at-text="5">5</a>
#                                                     </li><li data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-TTJEHU" class="au-target" au-target-id="327">
#                                                         <a href.bind="paginationUrl(page)" onclick="getElementById('eachJob').focus()" ph-tevent="pagination_click" role="button" key-aria-label="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultPaginationDynamicAriaLabelText" data-ph-at-id="pagination-page-number-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-ms3YtQ" class="au-target" au-target-id="328" href="https://careers.microsoft.com/us/en/search-results?keywords=php&amp;from=100&amp;s=1" data-ph-tevent-attr-trait214="6" aria-label="page 6" data-ph-at-text="6">6</a>
#                                                     </li><!--anchor-->
#                                                     <li data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-D7fLOK">
#                                                         <a href.bind="paginationUrl(currentSelectedPage + 1)" aria-label="View Next page" key-aria-label="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultBottomNextAriaLabelText" show.bind="nextButtonVisibility" ph-tevent="pagination_click" data-ph-tevent-attr-trait214="Next" role="button" key-role="oMJpEz-2fssdu-ph-search-results-v1-view-external-btnRole" data-ph-at-id="pagination-next-link" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-hclKdV" class="au-target" au-target-id="331" href="https://careers.microsoft.com/us/en/search-results?keywords=php&amp;from=20&amp;s=1">
#                                                             <ppc-content key="2fssdu-ph-search-results-v1-view-external-searchResultsShowingResultBottomNextText" data-ph-at-id="pagination-next-text" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-wXm0qV">
#            Next
#          </ppc-content>
#                                                             <ppc-content type="icon" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-StE6iW">
#                                                                 <span aria-hidden="true" class="icon icon-arrow-right" data-ph-id="ph-2fssdu-view-external-ph-search-results-v12fssdu-Jqai1g"></span>
#                                                             </ppc-content>
#                                                         </a>
#                                                     </li>
#                                                 </ul>
#                                             </div>
#                                             <!--End Bottom Pagination block -->
#                                         </div>
#                                     </div>
#                                     <!-- No jobs Found block-->
#                                     <!--anchor-->
#                                     <!--End Nojobs Found block-->
#                                 </div>
#                             <!--anchor--></div>
#        </section>
#        <!--End Search Results block-->
#       </div>
#       <!--End Right side block -->
#      </div>
#     </div>
#    </div>
#   </div>
#   <div class="ph-footer" data-ph-id="ph-page-element-page19-dhv1Vp"><section class="ph-widget ph-widget-layout ppc-section ph-widget-target" view="footer" type="static" instance-id="8onyzk" data-ph-id="footer-3Nxp7o" original-view="footer" as-element="footer" data-widget="footer"><div as-element="footer" data-widget="footer" view="footer" original-view="footer" type="static" instance-id="8onyzk" theme="default" class="ph-widget-target footer-default" data-ph-id="ph-page-element-footer-8onyzk-bUIpwT">
#  <footer data-ph-id="ph-page-element-footer-8onyzk-VpiSWx">
#   <div class="footer-block ph-widget-box" data-ph-id="ph-page-element-footer-8onyzk-QRF6Yk">
#    <div class="footer-top" data-ph-id="ph-page-element-footer-8onyzk-Ypj69B">
#     <div class="container" data-ph-id="ph-page-element-footer-8onyzk-2Cd0sk">
#      <ul data-ph-id="ph-page-element-footer-8onyzk-4csYoV">
#       <li data-ph-id="ph-page-element-footer-8onyzk-FIBEa9"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="faq" key-target="footer-TargetValue" target="_self" key-ph-href="footer-careersFaqLinkUrl" aria-label="FAQ" key-aria-label="footer-careersFaqLinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-Rx266R" role="link" class="au-target" au-target-id="36" href="/us/en/faq" data-ph-href="/us/en/faq"><i class="msicon-fullmdl2assets-23 options-icon" aria-hidden="true" data-ph-id="ph-page-element-footer-8onyzk-0lxREi"></i><span data-ph-id="ph-page-element-footer-8onyzk-Rg98vO">
#          <ppc-content type="text" key="footer-careersFaqLinkText" data-ph-id="ph-page-element-footer-8onyzk-MabgX1">FAQ</ppc-content> </span><i class="icon icon-arrow-right" aria-hidden="true" data-ph-id="ph-page-element-footer-8onyzk-dWSZ3X"></i></a> </li>
#       <li data-ph-id="ph-page-element-footer-8onyzk-9uSRy7"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="interview tips" key-ph-href="footer-careersInterViewTipsLinkUrl" aria-label="Interview tips" key-target="footer-careersInterViewTipsTargetValue" target="_self" key-aria-label="footer-careersInterViewTipsLinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-2Z01Na" role="link" class="au-target" au-target-id="37" href="/us/en/interviewtips" data-ph-href="/us/en/interviewtips"><i class="msicon-fullmdl2assets-36 options-icon" aria-hidden="true" data-ph-id="ph-page-element-footer-8onyzk-CPbOlK"></i><span data-ph-id="ph-page-element-footer-8onyzk-Ov4XXp">
#          <ppc-content type="text" key="footer-careersInterViewTipsLinkText" data-ph-id="ph-page-element-footer-8onyzk-Hvrt0d">Interview tips</ppc-content> </span><i class="icon icon-arrow-right" aria-hidden="true" data-ph-id="ph-page-element-footer-8onyzk-JVXkTs"></i></a> </li>
#       <li data-ph-id="ph-page-element-footer-8onyzk-oz60Ew"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Accessibility request" key-ph-href="footer-careersAccommodationRequestLinkUrl" aria-label="Accessibility request opens in a new tab" target="_blank" key-target="footer-careersAccommodationRequestTargetValue" key-aria-label="footer-careersAccommodationRequestLinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-tEHcv6" role="link" class="au-target" au-target-id="38" href="/us/en/accommodationrequest" data-ph-href="/us/en/accommodationrequest"><i class="msicon-fullmdl2assets-37 options-icon" aria-hidden="true" data-ph-id="ph-page-element-footer-8onyzk-UyrhOp"></i><span data-ph-id="ph-page-element-footer-8onyzk-zMG65v">
#          <ppc-content type="text" key="footer-careersAccommodationRequestLinkText" data-ph-id="ph-page-element-footer-8onyzk-PgyRvH">Accessibility request</ppc-content> </span><i class="icon icon-arrow-right" aria-hidden="true" data-ph-id="ph-page-element-footer-8onyzk-crYdnh"></i></a> </li>
#       <li data-ph-id="ph-page-element-footer-8onyzk-E1Qz0k"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="support" key-ph-href="footer-careersSupportLinkUrl" aria-label="Support opens in a new tab" target="_blank" key-target="footer-careersSupportTargetValue" key-aria-label="footer-careersSupportLinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-mayL0I" role="link" class="au-target" au-target-id="39" href="/us/en/support" data-ph-href="/us/en/support"><i class="msicon-fullmdl2assets-33 options-icon" aria-hidden="true" data-ph-id="ph-page-element-footer-8onyzk-owhpsW"></i><span data-ph-id="ph-page-element-footer-8onyzk-OuMYYW">
#          <ppc-content type="text" key="footer-careersSupportLinkText" data-ph-id="ph-page-element-footer-8onyzk-37ciEu">Support</ppc-content> </span><i class="icon icon-arrow-right" aria-hidden="true" data-ph-id="ph-page-element-footer-8onyzk-Ds1UxR"></i></a> </li>
#       <li data-ph-id="ph-page-element-footer-8onyzk-iKcDAl"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="legal policies" key-ph-href="footer-careersLegalLinkUrl" target="_self" key-target="footer-careersLegaTargetValue" kay-aria-label="careersLegalLinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-EGXKuL" role="link" class="au-target" au-target-id="40" href="/us/en/legalpolicies" data-ph-href="/us/en/legalpolicies"><i class="msicon-fullmdl2assets-35 options-icon" aria-hidden="true" data-ph-id="ph-page-element-footer-8onyzk-Bj4VWB"></i><span data-ph-id="ph-page-element-footer-8onyzk-I6hjLY">
#          <ppc-content type="text" key="footer-careersLegalLinkText" data-ph-id="ph-page-element-footer-8onyzk-RjJcwd">Legal policies</ppc-content> </span><i class="icon icon-arrow-right" aria-hidden="true" data-ph-id="ph-page-element-footer-8onyzk-6e3YxZ"></i></a> </li>
#       <li data-ph-id="ph-page-element-footer-8onyzk-svV4vy"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Microsoft Data Protection Notice (DPN)" key-href="footer-careersPandCLinkUrl" target="_blank" href="https://msdpn.azurewebsites.net/default?LID=62" key-target="footer-careersPandCTargetValue" aria-label="Microsoft Data Protection Notice (DPN)" key-aria-label="footer-careersPandCLinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-w2JCdk" role="link" class="au-target" au-target-id="41"><i class="msicon-fullmdl2assets-34 options-icon" aria-hidden="true" data-ph-id="ph-page-element-footer-8onyzk-ZZsDDV"></i><span data-ph-id="ph-page-element-footer-8onyzk-LEwGkj">
#          <ppc-content type="text" key="footer-careersPandCLinkText" data-ph-id="ph-page-element-footer-8onyzk-Jzotwk">Microsoft Data Protection Notice (DPN)</ppc-content> </span><i class="icon icon-arrow-right" aria-hidden="true" data-ph-id="ph-page-element-footer-8onyzk-PjN615"></i></a> </li>
#       <li data-ph-id="ph-page-element-footer-8onyzk-ecBhGh"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="feedback" href="https://aka.ms/CareersFeedback" key-href="footer-careersFeedbackLinkUrl" target="_blank" key-target="footer-careersFeedbackTargetValue" aria-label="Feedback opens in a new tab" key-aria-label="footer-careersFeedbackLinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-HlVXIx" role="link" class="au-target" au-target-id="42"><i class="msicon-fullmdl2assets-28 options-icon" aria-hidden="true" data-ph-id="ph-page-element-footer-8onyzk-CGaVf0"></i><span data-ph-id="ph-page-element-footer-8onyzk-OdgzTv">
#          <ppc-content key="footer-careersFeedbackLinkText" data-ph-id="ph-page-element-footer-8onyzk-FZ9g8n">Feedback</ppc-content> </span><i class="icon icon-arrow-right" aria-hidden="true" data-ph-id="ph-page-element-footer-8onyzk-4ayi3m"></i></a> </li>
#       <li class="hide" id="internalVisible" data-ph-id="ph-page-element-footer-8onyzk-45qwP3"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Labor Condition Application Postings" key-href="footer-careersLCANCLinkUrl" target="_blank" href="https://aka.ms/LCANotices" key-target="footer-careersLCANCTargetValue" aria-label="Labor Condition Application Postings opens in a new tab" key-aria-label="footer-careersLCANCLinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-D3D7QT" role="link" class="au-target" au-target-id="43"><img src="https://prodcmscdn.azureedge.net/careerconnectresources/p/MICRUS/en_us/desktop/assets/images/file_footer.png" aria-hidden="true" key-alt="footer-careersLCANCAltText" alt="" data-ph-id="ph-page-element-footer-8onyzk-eHt3Co"><span data-ph-id="ph-page-element-footer-8onyzk-pmwPSJ">
#          <ppc-content key="footer-careersLCANCLinkText" data-ph-id="ph-page-element-footer-8onyzk-J1n2YC">
#           Labor Condition Application Postings
#          </ppc-content> </span><i class="icon icon-arrow-right" aria-hidden="true" data-ph-id="ph-page-element-footer-8onyzk-Bp4MIZ"></i></a> </li>
#      </ul>
#     </div>
#    </div>
#    <div class="footer-social-media-icons" data-ph-id="ph-page-element-footer-8onyzk-MQvCKc">
#     <div class="container" data-ph-id="ph-page-element-footer-8onyzk-uA6HYc">
#      <div class="footer-social-header" data-ph-id="ph-page-element-footer-8onyzk-qr3x6c">
#       <h2 data-ph-id="ph-page-element-footer-8onyzk-0e6iDt">
#        <ppc-content key="footer-universalfollowMicrosoftCareersHadingText" data-ph-id="ph-page-element-footer-8onyzk-65zPsp">Follow Microsoft Careers</ppc-content> </h2>
#      </div>
#      <div class="footer-social-list" data-ph-id="ph-page-element-footer-8onyzk-XY5OBR">
#       <ul data-ph-id="ph-page-element-footer-8onyzk-YTFmh1">
#        <li class="linkedin" data-ph-id="ph-page-element-footer-8onyzk-rbFLDt"> <a ph-tevent="socialnetwork_menu_click" data-ph-tevent-attr-trait213="linkedin" key-href="footer-universalLinkedInLinkUrl" href="https://www.linkedin.com/company/microsoft" target="_blank" key-target="footer-universalLinkedTargetValue" aria-label="Follow Microsoft careers on LinkedIn opens in a new tab" key-aria-label="footer-universalLinkedInLinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-KaXmoO" role="link" class="au-target" au-target-id="44"> <img aria-hidden="true" tabindex="-1" src="https://prodcmscdn.azureedge.net/careerconnectresources/p/MICRUS/en_us/desktop/assets/images/linkedin-icon.svg" key-src="footer-universalLinkedInImgSrc" alt="LinkedIn logo" key-alt="footer-universalLinkedInAltText" class="img-responsive" title="LinkedIn" key-title="footer-universalLinkedInImgTitle" data-ph-id="ph-page-element-footer-8onyzk-y3KTpg"> </a> </li>
#        <li class="twitter" data-ph-id="ph-page-element-footer-8onyzk-kxZlD9"> <a ph-tevent="socialnetwork_menu_click" data-ph-tevent-attr-trait213="twitter" key-href="footer-universalTwitterLinkUrl" href="https://twitter.com/microsoft" target="_blank" key-target="footer-universalTwitterTargetValue" key-aria-label="footer-universalTwitterLinkLabelText" aria-label="Follow Microsoft careers on Twitter opens in a new tab" data-ph-id="ph-page-element-footer-8onyzk-Y133fJ" role="link" class="au-target" au-target-id="45">
#          <ppc-content type="image" data-ph-id="ph-page-element-footer-8onyzk-hL5ECV">
#           <img aria-hidden="true" tabindex="-1" src="https://prodcmscdn.azureedge.net/careerconnectresources/p/MICRUS/en_us/desktop/assets/images/twitter-icon.svg" key-src="footer-universalTwitterImgSrc" alt="Twitter logo" key-alt="footer-universalTwitterAltText" title="Twitter" key-title="footer-universalTwitterImgTitle" class="img-responsive" data-ph-id="ph-page-element-footer-8onyzk-1OKUx9">
#          </ppc-content> </a> </li>
#        <li class="facebook" data-ph-id="ph-page-element-footer-8onyzk-2ddH5n"> <a ph-tevent="socialnetwork_menu_click" data-ph-tevent-attr-trait213="facebook" key-href="footer-universalFacebookLinkUrl" href="https://www.facebook.com/Microsoft" target="_blank" key-target="footer-universalFacebookTargetValue" aria-label="Follow Microsoft careers on Facebook opens in a new tab" key-aria-label="footer-universalFacebookLinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-8EJjct" role="link" class="au-target" au-target-id="46">
#          <ppc-content type="image" data-ph-id="ph-page-element-footer-8onyzk-SlXcqY">
#           <img aria-hidden="true" tabindex="-1" src="https://prodcmscdn.azureedge.net/careerconnectresources/p/MICRUS/en_us/desktop/assets/images/fb-icon.svg" key-src="footer-universalFacebookImgSrc" alt="Facebook logo" key-alt="footer-universalFacebookAltText" title="Facebook" key-title="footer-universalFacebookImgTitle" class="img-responsive" data-ph-id="ph-page-element-footer-8onyzk-foVpFh">
#          </ppc-content> </a> </li>
#        <li class="instagram" data-ph-id="ph-page-element-footer-8onyzk-FGrfD8"> <a ph-tevent="socialnetwork_menu_click" data-ph-tevent-attr-trait213="instagram" key-href="footer-universalInstagramLinkUrl" href="https://www.instagram.com/microsoft" target="_blank" key-target="footer-universalInstagramTargetValue" aria-label="Follow Microsoft careers on Instagram opens in a new tab" key-aria-label="footer-universalInstagramLinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-N6hnNf" role="link" class="au-target" au-target-id="47">
#          <ppc-content type="image" data-ph-id="ph-page-element-footer-8onyzk-BvtDoK">
#           <img aria-hidden="true" tabindex="-1" src="https://prodcmscdn.azureedge.net/careerconnectresources/p/MICRUS/en_us/desktop/assets/images/Instagram-icon.svg" key-src="footer-universalInstagramImgSrc" alt="Instagram logo" key-alt="footer-universalInstagramAltText" title="Instagram" key-title="footer-universalInstagramImgTitle" class="img-responsive" data-ph-id="ph-page-element-footer-8onyzk-w4k9yo">
#          </ppc-content> </a> </li>
#       </ul>
#      </div>
#      <div class="language-block" data-ph-id="ph-page-element-footer-8onyzk-2Rv8a8">
#       <section class="ph-widget ppc-section ph-widget-layout" instance-id="eqfhjt" data-ph-id="ph-page-element-footer-8onyzk-46mZBK">
#        <div as-element="ph-language-selector-v1" data-widget="ph-language-selector-v1" class="ph-language-selector-v1-language-link-default ph-widget-target au-target" view="1564397942232-language-link" theme="default" instance-id="eqfhjt" data-ph-id="ph-page-element-footer-8onyzk-Kcudjw" original-view="language-link" au-target-id="48">
#
#                                     <div ph-loading-img="show-loader.bind: showLoader" show.bind="showLoader" class="show-loader au-target aurelia-hide" data-ph-id="ph-page-element-footer-eqfhjt-fQJ8Me" au-target-id="333"></div>
#                                     <div class="phs-lang-select-area ph-widget-box au-target" show.bind="!showLoader" data-ph-id="ph-page-element-footer-eqfhjt-wBx3MK" au-target-id="334">
#                                         <div class="phs-lang-select-list" data-ph-id="ph-page-element-footer-eqfhjt-rgR2q5">
#                                             <ul data-ph-id="ph-page-element-footer-eqfhjt-X0KzyG">
#                                                 <li data-ph-id="ph-page-element-footer-eqfhjt-KK3YeB">
#                                                     <a href="javascript:void(0)" click.delegate="languageChanged(lang)" data-ph-id="ph-page-element-footer-eqfhjt-JQav0j" class="au-target active" au-target-id="335" aria-label="Redirects to  Version of Site">
#                                                         <img aria-hidden="true" data-ph-id="ph-page-element-footer-eqfhjt-WYUiM2" class="au-target" au-target-id="336" alt=" icon" src="https://prodcmscdn.azureedge.net/careerconnectresources/p/MICRUS/en_us/desktop/assets/images/en_us.png">
#                                                         <span data-ph-id="ph-page-element-footer-eqfhjt-sUIiQL">EN</span>
#                                                     </a>
#                                                 </li><li data-ph-id="ph-page-element-footer-eqfhjt-KK3YeB">
#                                                     <a href="javascript:void(0)" click.delegate="languageChanged(lang)" data-ph-id="ph-page-element-footer-eqfhjt-JQav0j" class="au-target" au-target-id="335" aria-label="Redirects to  Version of Site">
#                                                         <img aria-hidden="true" data-ph-id="ph-page-element-footer-eqfhjt-WYUiM2" class="au-target" au-target-id="336" alt=" icon" src="https://prodcmscdn.azureedge.net/careerconnectresources/p/MICRUS/en_us/desktop/assets/images/fr_ca.png">
#                                                         <span data-ph-id="ph-page-element-footer-eqfhjt-sUIiQL">FR</span>
#                                                     </a>
#                                                 </li><!--anchor-->
#                                             </ul>
#                                         </div>
#                                     </div>
#                                 <!--anchor--></div>
#       </section>
#      </div>
#     </div>
#    </div>
#    <div class="shell-footer" data-ph-id="ph-page-element-footer-8onyzk-YISQ01">
#     <div class="shell-footer-wrapper" data-ph-id="ph-page-element-footer-8onyzk-QTtmP6">
#      <div class="shell-footer-menugroups" id="footer-nav" data-ph-id="ph-page-element-footer-8onyzk-UcxHRA">
#       <div class="sfm-group" data-ph-id="ph-page-element-footer-8onyzk-IXqrSq">
#        <div class="group-title" data-ph-id="ph-page-element-footer-8onyzk-F9YqK1">
#         <h2 data-ph-id="ph-page-element-footer-8onyzk-tikpXO">
#          <ppc-content key="footer-newUniversalWhatsNewHeadingText" data-ph-id="ph-page-element-footer-8onyzk-W8Pf17">
#           What's new
#          </ppc-content> </h2>
#        </div>
#        <button role="button" id="Learn-navigation" aria-expanded="false" class="footer-menubtn" onclick="ph$Msft$Custom.footer_Menu_open(this)" onfocus="ph$Msft$Custom.footer_Menu_onFocus(this)" aria-label="What's new" key-aria-label="footer-newUniversalWhatsNewBtnLabelText" data-ph-id="ph-page-element-footer-8onyzk-jODsoi">
#         <ppc-content key="footer-newUniversalWhatsNewBtnText" data-ph-id="ph-page-element-footer-8onyzk-y3IeS8">
#          What's new
#         </ppc-content> <i class="icon icon-down-arrow" aria-hidden="true" data-ph-id="ph-page-element-footer-8onyzk-zQOYF4"></i> </button>
#        <ul class="footer-menupanel" aria-labelledby="Learn-navigation" data-ph-id="ph-page-element-footer-8onyzk-DgTVvX">
#         <li data-ph-id="ph-page-element-footer-8onyzk-Pdl0Bi"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="NEW Surface Pro 6" class="footer-click au-target" key-href="footer-newUniversalWhatsNewList1LinkUrl" href="https://www.microsoft.com/en-us/p/surface-pro-6/8ZCNC665SLQ5" target="_blank" key-target="footer-newUniversalWhatsNewList1TargetValue" aria-label="NEW Surface Pro 6 opens in a new tab" key-aria-label="footer-newUniversalWhatsNewList1LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-hoNBER" role="link" au-target-id="49">
#           <ppc-content key="footer-newUniversalWhatsNewList1LinkText" data-ph-id="ph-page-element-footer-8onyzk-WICupE">
#            NEW Surface Pro 6
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-adEHyy"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="NEW Surface Laptop 2" class="footer-click au-target" key-href="footer-newUniversalWhatsNewList2LinkUrl" href="https://www.microsoft.com/en-us/p/surface-laptop-2/8XQJKK3DD91B" target="_blank" key-target="footer-newUniversalWhatsNewList2TargetValue" aria-label="NEW Surface Laptop 2 opens in a new tab" key-aria-label="footer-newUniversalWhatsNewList2LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-gxO5cQ" role="link" au-target-id="50">
#           <ppc-content key="footer-newUniversalWhatsNewList2LinkText" data-ph-id="ph-page-element-footer-8onyzk-3KGxBD">
#            NEW Surface Laptop 2
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-LdJION"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="NEW Surface Go" class="footer-click au-target" key-href="footer-newUniversalWhatsNewList3LinkUrl" href="https://www.microsoft.com/p/surface-go/8v9dp4lnknsz" target="_blank" key-target="footer-newUniversalWhatsNewList3TargetValue" aria-label="NEW Surface Go opens in a new tab" key-aria-label="footer-newUniversalWhatsNewList3LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-B5tuRb" role="link" au-target-id="51">
#           <ppc-content key="footer-newUniversalWhatsNewList3LinkText" data-ph-id="ph-page-element-footer-8onyzk-XY9I9y">
#            NEW Surface Go
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-EsVu7y"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Xbox One X" class="footer-click au-target" key-href="footer-newUniversalWhatsNewList4LinkUrl" href="https://www.xbox.com/en-us/xbox-one-x" target="_blank" key-target="footer-newUniversalWhatsNewList4TargetValue" aria-label="Xbox One X opens in a new tab" key-aria-label="footer-newUniversalWhatsNewList4LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-bckvqq" role="link" au-target-id="52">
#           <ppc-content key="footer-newUniversalWhatsNewList4LinkText" data-ph-id="ph-page-element-footer-8onyzk-WD4vFj">
#            Xbox One X
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-VK7rGZ"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Xbox One S" class="footer-click au-target" key-href="footer-newUniversalWhatsNewList5LinkUrl" href="https://www.xbox.com/en-us/xbox-one-s?xr=shellnav" target="_blank" key-target="footer-newUniversalWhatsNewList5TargetValue" aria-label="Xbox One S opens in a new tab" key-aria-label="footer-newUniversalWhatsNewList5LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-LlleUM" role="link" au-target-id="53">
#           <ppc-content key="footer-newUniversalWhatsNewList5LinkText" data-ph-id="ph-page-element-footer-8onyzk-2oqgyZ">
#            Xbox One S
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-w6BrOv"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="VR &amp; mixed reality" class="footer-click au-target" key-href="footer-newUniversalWhatsNewList6LinkUrl" href="https://www.microsoft.com/en-us/store/b/virtualreality" target="_blank" key-target="footer-newUniversalWhatsNewList6TargetValue" aria-label="VR &amp; mixed reality opens in a new tab" key-aria-label="footer-newUniversalWhatsNewList6LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-4WnXx9" role="link" au-target-id="54">
#           <ppc-content key="footer-newUniversalWhatsNewList6LinkText" data-ph-id="ph-page-element-footer-8onyzk-F7xiZm">
#            VR &amp; mixed reality
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-SdP498"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Windows 10 apps" class="footer-click au-target" key-href="footer-newUniversalWhatsNewList7LinkUrl" href="https://www.microsoft.com/en-us/windows/windows-10-apps" target="_blank" key-target="footer-newUniversalWhatsNewList7TargetValue" aria-label="Windows 10 apps opens in a new tab" key-aria-label="footer-newUniversalWhatsNewList7LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-TQtes7" role="link" au-target-id="55">
#           <ppc-content key="footer-newUniversalWhatsNewList7LinkText" data-ph-id="ph-page-element-footer-8onyzk-1XW11f">
#            Windows 10 apps
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-b7khMN"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Office apps" class="footer-click au-target" key-href="footer-newUniversalWhatsNewList8LinkUrl" href="https://store.office.com/en-us/appshome.aspx?" target="_blank" key-target="footer-newUniversalWhatsNewList8TargetValue" aria-label="Office apps opens in a new tab" key-aria-label="footer-newUniversalWhatsNewList8LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-yfxyR2" role="link" au-target-id="56">
#           <ppc-content key="footer-newUniversalWhatsNewList8LinkText" data-ph-id="ph-page-element-footer-8onyzk-v9IFYA">
#            Office apps
#           </ppc-content> </a> </li>
#        </ul>
#       </div>
#       <div class="sfm-group" data-ph-id="ph-page-element-footer-8onyzk-dIEeEO">
#        <div class="group-title" data-ph-id="ph-page-element-footer-8onyzk-LroxmB">
#         <h2 data-ph-id="ph-page-element-footer-8onyzk-9kNSBW">
#          <ppc-content key="footer-newUniversalStoreAndSupportHeadingText" data-ph-id="ph-page-element-footer-8onyzk-cjYlQv">
#           Store &amp; Support
#          </ppc-content> </h2>
#        </div>
#        <button role="button" id="Dev-navigation" aria-expanded="false" class="footer-menubtn" onclick="ph$Msft$Custom.footer_Menu_open(this)" onfocus="ph$Msft$Custom.footer_Menu_onFocus(this)" aria-label="Store &amp; Support" key-aria-label="footer-newUniversalStoreAndSupportBtnLabelText" data-ph-id="ph-page-element-footer-8onyzk-Fg2cqJ">
#         <ppc-content key="footer-newUniversalStoreAndSupportBtnText" data-ph-id="ph-page-element-footer-8onyzk-PnowrL">
#          Store &amp; Support
#         </ppc-content><i class="icon icon-down-arrow" aria-hidden="true" data-ph-id="ph-page-element-footer-8onyzk-jHnjD7"></i> </button>
#        <ul class="footer-menupanel" aria-labelledby="Dev-navigation" data-ph-id="ph-page-element-footer-8onyzk-6EELmk">
#         <li data-ph-id="ph-page-element-footer-8onyzk-Khay1d"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Account profile" class="footer-click au-target" key-href="footer-newUniversalStoreAndSupportList1LinkUrl" href="https://account.microsoft.com/" target="_blank" key-target="footer-newUniversalStoreAndSupportList1TargetValue" aria-label="Account profile opens in a new tab" key-aria-label="footer-newUniversalStoreAndSupportList1LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-OBqJpv" role="link" au-target-id="57">
#           <ppc-content key="footer-newUniversalStoreAndSupportList1LinkText" data-ph-id="ph-page-element-footer-8onyzk-1vunrY">
#            Account profile
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-SlgLu4"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Download Center" class="footer-click au-target" key-href="footer-newUniversalStoreAndSupportList2LinkUrl" href="https://www.microsoft.com/en-us/download" target="_blank" key-target="footer-newUniversalStoreAndSupportList2TargetValue" aria-label="Download Center opens in a new tab" key-aria-label="footer-newUniversalStoreAndSupportList2LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-fvEFaJ" role="link" au-target-id="58">
#           <ppc-content key="footer-newUniversalStoreAndSupportList2LinkText" data-ph-id="ph-page-element-footer-8onyzk-O1DvDi">
#            Download Center
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-9Yo2CV"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Sales &amp; support" class="footer-click au-target" key-href="footer-newUniversalStoreAndSupportList3LinkUrl" href="https://go.microsoft.com/fwlink/p/?LinkID=824761&amp;clcid=0x409" target="_blank" key-target="footer-newUniversalStoreAndSupportList3TargetValue" aria-label="Sales &amp; support opens in a new tab" key-aria-label="footer-newUniversalStoreAndSupportList3LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-McpJB0" role="link" au-target-id="59">
#           <ppc-content key="footer-newUniversalStoreAndSupportList3LinkText" data-ph-id="ph-page-element-footer-8onyzk-7q4x1z">
#            Sales &amp; support
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-3xjaEg"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Returns" class="footer-click au-target" key-href="footer-newUniversalStoreAndSupportList4LinkUrl" href="https://go.microsoft.com/fwlink/p/?LinkID=824764&amp;clcid=0x409" target="_blank" key-target="footer-newUniversalStoreAndSupportList4TargetValue" aria-label="Returns opens in a new tab" key-aria-label="footer-newUniversalStoreAndSupportList4LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-Cpw6E5" role="link" au-target-id="60">
#           <ppc-content key="footer-newUniversalStoreAndSupportList4LinkText" data-ph-id="ph-page-element-footer-8onyzk-0D7eZv">
#            Returns
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-jcDuEY"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Order tracking" class="footer-click au-target" key-href="footer-newUniversalStoreAndSupportList5LinkUrl" href="https://account.microsoft.com/orders" target="_blank" key-target="footer-newUniversalStoreAndSupportList5TargetValue" aria-label="Order tracking opens in a new tab" key-aria-label="footer-newUniversalStoreAndSupportList5LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-6xqPoC" role="link" au-target-id="61">
#           <ppc-content key="footer-newUniversalStoreAndSupportList5LinkText" data-ph-id="ph-page-element-footer-8onyzk-BhZH5g">
#            Order tracking
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-p6nQbd"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Store locations" class="footer-click au-target" key-href="footer-newUniversalStoreAndSupportList6LinkUrl" href="https://www.microsoft.com/en-us/store/locations/find-a-store?icid=en-us_UF_FAS" target="_blank" key-target="footer-newUniversalStoreAndSupportList6TargetValue" aria-label="Store locations opens in a new tab" key-aria-label="footer-newUniversalStoreAndSupportList6LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-A2rHbD" role="link" au-target-id="62">
#           <ppc-content key="footer-newUniversalStoreAndSupportList6LinkText" data-ph-id="ph-page-element-footer-8onyzk-RqEkVE">
#            Store locations
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-aPekRC"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Support" class="footer-click au-target" key-href="footer-newUniversalStoreAndSupportList7LinkUrl" href="https://support.microsoft.com/en-us" target="_blank" key-target="footer-newUniversalStoreAndSupportList7TargetValue" aria-label="Support opens in a new tab" key-aria-label="footer-newUniversalStoreAndSupportList7LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-UVxSTR" role="link" au-target-id="63">
#           <ppc-content key="footer-newUniversalStoreAndSupportList7LinkText" data-ph-id="ph-page-element-footer-8onyzk-2sh83u">
#            Support
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-zDhlW2"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Buy online, pick up in store" class="footer-click au-target" key-href="footer-newUniversalStoreAndSupportList8LinkUrl" href="https://www.microsoft.com/en-us/store/b/buy-online-pick-up-in-store?icid=uhf_footer_bopuis" target="_blank" key-target="footer-newUniversalStoreAndSupportList8TargetValue" aria-label="Buy online, pick up in store opens in a new tab" key-aria-label="footer-newUniversalStoreAndSupportList8LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-JdxMEd" role="link" au-target-id="64">
#           <ppc-content key="footer-newUniversalStoreAndSupportList8LinkText" data-ph-id="ph-page-element-footer-8onyzk-u6VrzR">
#            Buy online, pick up in store
#           </ppc-content> </a> </li>
#        </ul>
#       </div>
#       <div class="sfm-group" data-ph-id="ph-page-element-footer-8onyzk-o8FvUP">
#        <div class="group-title" data-ph-id="ph-page-element-footer-8onyzk-3yiwOf">
#         <h2 data-ph-id="ph-page-element-footer-8onyzk-UWbhFU">
#          <ppc-content type="text" key="footer-newUniversalEducationHeadingText" data-ph-id="ph-page-element-footer-8onyzk-9WjdFM">
#           Education
#          </ppc-content> </h2>
#        </div>
#        <button role="button" id="Ms-navigation" aria-expanded="false" class="footer-menubtn" onclick="ph$Msft$Custom.footer_Menu_open(this)" onfocus="ph$Msft$Custom.footer_Menu_onFocus(this)" aria-label="Education" key-aria-label="footer-newUniversalEducationBtnLabelText" data-ph-id="ph-page-element-footer-8onyzk-jH87Yo">
#         <ppc-content key="footer-newUniversalEducationBtnText" data-ph-id="ph-page-element-footer-8onyzk-3WRfg5">
#          Education
#         </ppc-content><i class="icon icon-down-arrow" aria-hidden="true" data-ph-id="ph-page-element-footer-8onyzk-xxXOxV"></i> </button>
#        <ul class="footer-menupanel" aria-labelledby="Ms-navigation" data-ph-id="ph-page-element-footer-8onyzk-xHh7bG">
#         <li data-ph-id="ph-page-element-footer-8onyzk-tPBndD"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Microsoft in education" class="footer-click au-target" key-href="footer-newUniversalEducationList1LinkUrl" href="https://www.microsoft.com/en-us/education" target="_blank" key-target="footer-newUniversalEducationList1TargetValue" aria-label="Microsoft in education opens in a new tab" key-aria-label="footer-newUniversalEducationList1LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-ooJFo0" role="link" au-target-id="65">
#           <ppc-content key="footer-newUniversalEducationList1LinkText" data-ph-id="ph-page-element-footer-8onyzk-KWC5ob">
#            Microsoft in education
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-Drt3H9"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Office for students" class="footer-click au-target" key-href="footer-newUniversalEducationList2LinkUrl" href="https://www.microsoft.com/en-us/education/products/office/default.aspx" target="_blank" key-target="footer-newUniversalEducationList2TargetValue" aria-label="Office for students opens in a new tab" key-aria-label="footer-newUniversalEducationList2LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-wFYhbC" role="link" au-target-id="66">
#           <ppc-content key="footer-newUniversalEducationList2LinkText" data-ph-id="ph-page-element-footer-8onyzk-bxacaN">
#            Office for students
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-l66uTK"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Office 365 for schools" class="footer-click au-target" key-href="footer-newUniversalEducationList3LinkUrl" href="https://products.office.com/en-us/academic/compare-office-365-education-plans" target="_blank" key-target="footer-newUniversalEducationList3TargetValue" aria-label="Office 365 for schools opens in a new tab" key-aria-label="footer-newUniversalEducationList3LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-tXxmWl" role="link" au-target-id="67">
#           <ppc-content key="footer-newUniversalEducationList3LinkText" data-ph-id="ph-page-element-footer-8onyzk-j4rR4R">
#            Office 365 for schools
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-GBwICJ"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Deals for students &amp; parents" class="footer-click au-target" key-href="footer-newUniversalEducationList4LinkUrl" href="https://www.microsoft.com/en-us/store/b/education?icid=CNavfooter_Studentsandeducation" target="_blank" key-target="footer-newUniversalEducationList4TargetValue" aria-label="Deals for students &amp; parents opens in a new tab" key-aria-label="footer-newUniversalEducationList4LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-ie4Crw" role="link" au-target-id="68">
#           <ppc-content key="footer-newUniversalEducationList4LinkText" data-ph-id="ph-page-element-footer-8onyzk-XJSwhR">
#            Deals for students &amp; parents
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-d3R6xA"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Microsoft Azure in education" class="footer-click au-target" key-href="footer-newUniversalEducationList5LinkUrl" href="https://azure.microsoft.com/en-us/community/education/" target="_blank" key-target="footer-newUniversalEducationList5TargetValue" aria-label="Microsoft Azure in education opens in a new tab" key-aria-label="footer-newUniversalEducationList5LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-kYvZHU" role="link" au-target-id="69">
#           <ppc-content key="footer-newUniversalEducationList5LinkText" data-ph-id="ph-page-element-footer-8onyzk-jpPxKq">
#            Microsoft Azure in education
#           </ppc-content> </a> </li>
#        </ul>
#       </div>
#       <div class="sfm-group" data-ph-id="ph-page-element-footer-8onyzk-GkhQDK">
#        <div class="group-title" data-ph-id="ph-page-element-footer-8onyzk-lHk5WI">
#         <h2 data-ph-id="ph-page-element-footer-8onyzk-Q6NupM">
#          <ppc-content type="text" key="footer-newUniversalEnterpriseHeadingText" data-ph-id="ph-page-element-footer-8onyzk-aCBtKM">
#           Enterprise
#          </ppc-content> </h2>
#        </div>
#        <button role="button" id="dwn-navigation" aria-expanded="false" class="footer-menubtn" onclick="ph$Msft$Custom.footer_Menu_open(this)" onfocus="ph$Msft$Custom.footer_Menu_onFocus(this)" aria-label="Enterprise" key-aria-label="footer-newUniversalEnterpriseBtnLabelText" data-ph-id="ph-page-element-footer-8onyzk-kxc29K">
#         <ppc-content key="footer-newUniversalEnterpriseBtnText" data-ph-id="ph-page-element-footer-8onyzk-QLuXbp">
#          Enterprise
#         </ppc-content><i class="icon icon-down-arrow" aria-hidden="true" data-ph-id="ph-page-element-footer-8onyzk-jK6Ysw"></i> </button>
#        <ul class="footer-menupanel" aria-labelledby="dwn-navigation" data-ph-id="ph-page-element-footer-8onyzk-V7C4N7">
#         <li data-ph-id="ph-page-element-footer-8onyzk-gT7wHy"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Microsoft Azure" class="footer-click au-target" key-href="footer-newUniversalEnterpriseList1LinkUrl" href="https://azure.microsoft.com/" target="_blank" key-target="footer-newUniversalEnterpriseList1TargetValue" aria-label="Microsoft Azure opens in a new tab" key-aria-label="footer-newUniversalEnterpriseList1LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-FWTg04" role="link" au-target-id="70">
#           <ppc-content key="footer-newUniversalEnterpriseList1LinkText" data-ph-id="ph-page-element-footer-8onyzk-IOwsUc">
#            Microsoft Azure
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-qooBB3"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Microsoft Industry" class="footer-click au-target" key-href="footer-newUniversalEnterpriseList2LinkUrl" href="https://enterprise.microsoft.com/en-us/" target="_blank" key-target="footer-newUniversalEnterpriseList2TargetValue" aria-label="Microsoft Industry opens in a new tab" key-aria-label="footer-newUniversalEnterpriseList2LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-K11IAe" role="link" au-target-id="71">
#           <ppc-content key="footer-newUniversalEnterpriseList2LinkText" data-ph-id="ph-page-element-footer-8onyzk-11kPce">
#            Microsoft Industry
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-h5m8HE"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Data platform" class="footer-click au-target" key-href="footer-newUniversalEnterpriseList3LinkUrl" href="https://www.microsoft.com/en-us/sql-server/" target="_blank" key-target="footer-newUniversalEnterpriseList3TargetValue" aria-label="Data platform opens in a new tab" key-aria-label="footer-newUniversalEnterpriseList3LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-jZW2UR" role="link" au-target-id="72">
#           <ppc-content key="footer-newUniversalEnterpriseList3LinkText" data-ph-id="ph-page-element-footer-8onyzk-4es40J">
#            Data platform
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-klqc86"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Find a solution provider" class="footer-click au-target" key-href="footer-newUniversalEnterpriseList4LinkUrl" href="https://www.microsoft.com/en-us/solution-providers" target="_blank" key-target="footer-newUniversalEnterpriseList4TargetValue" aria-label="Find a solution provider opens in a new tab" key-aria-label="footer-newUniversalEnterpriseList4LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-7t0W5y" role="link" au-target-id="73">
#           <ppc-content key="footer-newUniversalEnterpriseList4LinkText" data-ph-id="ph-page-element-footer-8onyzk-U5HpSA">
#            Find a solution provider
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-jaN5kf"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Microsoft partner resources" class="footer-click au-target" key-href="footer-newUniversalEnterpriseList5LinkUrl" href="https://partner.microsoft.com/en-us/" target="_blank" key-target="footer-newUniversalEnterpriseList5TargetValue" aria-label="Microsoft partner resources opens in a new tab" key-aria-label="footer-newUniversalEnterpriseList5LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-PJ0MZf" role="link" au-target-id="74">
#           <ppc-content key="footer-newUniversalEnterpriseList5LinkText" data-ph-id="ph-page-element-footer-8onyzk-XyFOA7">
#            Microsoft partner resources
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-hCAs32"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Microsoft AppSource" class="footer-click au-target" key-href="footer-newUniversalEnterpriseList6LinkUrl" href="https://go.microsoft.com/fwlink/?LinkID=808093" target="_blank" key-target="footer-newUniversalEnterpriseList6TargetValue" aria-label="Microsoft AppSource opens in a new tab" key-aria-label="footer-newUniversalEnterpriseList6LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-95ToyK" role="link" au-target-id="75">
#           <ppc-content key="footer-newUniversalEnterpriseList6LinkText" data-ph-id="ph-page-element-footer-8onyzk-AUzsx9">
#            Microsoft AppSource
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-JQdwdX"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Health" class="footer-click au-target" key-href="footer-newUniversalEnterpriseList7LinkUrl" href="https://www.microsoft.com/en-us/enterprise/health" target="_blank" key-target="footer-newUniversalEnterpriseList7TargetValue" aria-label="Health opens in a new tab" key-aria-label="footer-newUniversalEnterpriseList7LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-oGxwrY" role="link" au-target-id="76">
#           <ppc-content key="footer-newUniversalEnterpriseList7LinkText" data-ph-id="ph-page-element-footer-8onyzk-6IxX4I">
#            Health
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-3ePcCn"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Financial services" class="footer-click au-target" key-href="footer-newUniversalEnterpriseList8LinkUrl" href="https://www.microsoft.com/en-us/enterprise/finance/banking-capital-markets" target="_blank" key-target="footer-newUniversalEnterpriseList8TargetValue" aria-label="Financial services opens in a new tab" key-aria-label="footer-newUniversalEnterpriseList8LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-JmM3lI" role="link" au-target-id="77">
#           <ppc-content key="footer-newUniversalEnterpriseList8LinkText" data-ph-id="ph-page-element-footer-8onyzk-p7turs">
#            Financial services
#           </ppc-content> </a> </li>
#        </ul>
#       </div>
#       <div class="sfm-group" data-ph-id="ph-page-element-footer-8onyzk-KS4MIq">
#        <div class="group-title" data-ph-id="ph-page-element-footer-8onyzk-Gk1Gz5">
#         <h2 data-ph-id="ph-page-element-footer-8onyzk-bkopSu">
#          <ppc-content type="text" key="footer-newUniversalDeveloperHeadingText" data-ph-id="ph-page-element-footer-8onyzk-MMoFPw">
#           Developer
#          </ppc-content> </h2>
#        </div>
#        <button role="button" id="val-navigation" aria-expanded="false" class="footer-menubtn" onclick="ph$Msft$Custom.footer_Menu_open(this)" onfocus="ph$Msft$Custom.footer_Menu_onFocus(this)" aria-label="Developer" key-aria-label="footer-newUniversalDeveloperBtnLabelText" data-ph-id="ph-page-element-footer-8onyzk-xUL4KU">
#         <ppc-content key="footer-newUniversalDeveloperBtnText" data-ph-id="ph-page-element-footer-8onyzk-O9K4y3">
#          Developer
#         </ppc-content><i class="icon icon-down-arrow" aria-hidden="true" data-ph-id="ph-page-element-footer-8onyzk-jfmDd3"></i> </button>
#        <ul class="footer-menupanel" aria-labelledby="val-navigation" data-ph-id="ph-page-element-footer-8onyzk-11Y1N8">
#         <li data-ph-id="ph-page-element-footer-8onyzk-5WtKZN"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Microsoft Visual Studio" class="footer-click au-target" key-href="footer-newUniversalDeveloperList1LinkUrl" href="https://visualstudio.microsoft.com/" target="_blank" key-target="footer-newUniversalDeveloperList1TargetValue" aria-label="Microsoft Visual Studio opens in a new tab" key-aria-label="footer-newUniversalDeveloperList1LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-gUYTNb" role="link" au-target-id="78">
#           <ppc-content key="footer-newUniversalDeveloperList1LinkText" data-ph-id="ph-page-element-footer-8onyzk-nJdIvS">
#            Microsoft Visual Studio
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-4xzlak"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Windows Dev Center" class="footer-click au-target" key-href="footer-newUniversalDeveloperList2LinkUrl" href="https://developer.microsoft.com/en-us/windows" target="_blank" key-target="footer-newUniversalDeveloperList2TargetValue" aria-label="Windows Dev Center opens in a new tab" key-aria-label="footer-newUniversalDeveloperList2LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-pPpFL5" role="link" au-target-id="79">
#           <ppc-content key="footer-newUniversalDeveloperList2LinkText" data-ph-id="ph-page-element-footer-8onyzk-NeeHqZ">
#            Windows Dev Center
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-Vi5XWQ"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Developer Network" class="footer-click au-target" key-href="footer-newUniversalDeveloperList3LinkUrl" href="https://msdn.microsoft.com/en-us" target="_blank" key-target="footer-newUniversalDeveloperList3TargetValue" aria-label="Developer Network opens in a new tab" key-aria-label="footer-newUniversalDeveloperList3LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-gNz89t" role="link" au-target-id="80">
#           <ppc-content key="footer-newUniversalDeveloperList3LinkText" data-ph-id="ph-page-element-footer-8onyzk-gCy4QM">
#            Developer Network
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-34UQhO"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="TechNet" class="footer-click au-target" key-href="footer-newUniversalDeveloperList4LinkUrl" href="https://technet.microsoft.com/en-us" target="_blank" key-target="footer-newUniversalDeveloperList4TargetValue" aria-label="TechNet opens in a new tab" key-aria-label="footer-newUniversalDeveloperList4LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-KeZSjz" role="link" au-target-id="81">
#           <ppc-content key="footer-newUniversalDeveloperList4LinkText" data-ph-id="ph-page-element-footer-8onyzk-viTL10">
#            TechNet
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-YBfcv1"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Microsoft developer program" class="footer-click au-target" key-href="footer-newUniversalDeveloperList5LinkUrl" href="https://developer.microsoft.com/en-us/store/register" target="_blank" key-target="footer-newUniversalDeveloperList5TargetValue" aria-label="Microsoft developer program opens in a new tab" key-aria-label="footer-newUniversalDeveloperList5LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-H5qvma" role="link" au-target-id="82">
#           <ppc-content key="footer-newUniversalDeveloperList5LinkText" data-ph-id="ph-page-element-footer-8onyzk-Hm7UvO">
#            Microsoft developer program
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-0bmO33"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Channel 9" class="footer-click au-target" key-href="footer-newUniversalDeveloperList6LinkUrl" href="https://channel9.msdn.com/" target="_blank" key-target="footer-newUniversalDeveloperList6TargetValue" aria-label="Channel 9 opens in a new tab" key-aria-label="footer-newUniversalDeveloperList6LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-nmzsxI" role="link" au-target-id="83">
#           <ppc-content key="footer-newUniversalDeveloperList6LinkText" data-ph-id="ph-page-element-footer-8onyzk-l2huYS">
#            Channel 9
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-5O4rH5"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Office Dev Center" class="footer-click au-target" key-href="footer-newUniversalDeveloperList7LinkUrl" href="https://developer.microsoft.com/en-us/office" target="_blank" key-target="footer-newUniversalDeveloperList7TargetValue" aria-label="Office Dev Center opens in a new tab" key-aria-label="footer-newUniversalDeveloperList7LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-2fqwV4" role="link" au-target-id="84">
#           <ppc-content key="footer-newUniversalDeveloperList7LinkText" data-ph-id="ph-page-element-footer-8onyzk-W6fwGg">
#            Office Dev Center
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-ZMK6ri"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Microsoft Garage" class="footer-click au-target" key-href="footer-newUniversalDeveloperList8LinkUrl" href="https://www.microsoft.com/en-us/garage/" target="_blank" key-target="footer-newUniversalDeveloperList8TargetValue" aria-label="Microsoft Garage opens in a new tab" key-aria-label="footer-newUniversalDeveloperList8LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-mQF1rx" role="link" au-target-id="85">
#           <ppc-content key="footer-newUniversalDeveloperList8LinkText" data-ph-id="ph-page-element-footer-8onyzk-fpszhy">
#            Microsoft Garage
#           </ppc-content> </a> </li>
#        </ul>
#       </div>
#       <div class="sfm-group" data-ph-id="ph-page-element-footer-8onyzk-2B0BwD">
#        <div class="group-title" data-ph-id="ph-page-element-footer-8onyzk-ytKJXa">
#         <h2 data-ph-id="ph-page-element-footer-8onyzk-sBfkl1">
#          <ppc-content type="text" key="footer-newUniversalCompanyHeadingText" data-ph-id="ph-page-element-footer-8onyzk-Fbf7Wp">
#            Company
#          </ppc-content> </h2>
#        </div>
#        <button role="button" id="comp-navigation" aria-expanded="false" class="footer-menubtn" onclick="ph$Msft$Custom.footer_Menu_open(this)" onfocus="ph$Msft$Custom.footer_Menu_onFocus(this)" aria-label="Company" key-aria-label="footer-newUniversalCompanyBtnLabelText" data-ph-id="ph-page-element-footer-8onyzk-DCZuQT">
#         <ppc-content key="footer-newUniversalCompanyBtnText" data-ph-id="ph-page-element-footer-8onyzk-WYgBuw">
#          Company
#         </ppc-content><i class="icon icon-down-arrow" aria-hidden="true" data-ph-id="ph-page-element-footer-8onyzk-dcYplH"></i> </button>
#        <ul class="footer-menupanel" aria-labelledby="comp-navigation" data-ph-id="ph-page-element-footer-8onyzk-aHGNX6">
#         <li data-ph-id="ph-page-element-footer-8onyzk-hY1TXO"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Careers" target="_self" key-target="footer-newUniversalCompanyList1TargetValue" aria-label="Careers" key-aria-label="footer-newUniversalCompanyList1LinkLabel" data-ph-id="ph-page-element-footer-8onyzk-XJ0guO" role="link" class="au-target" au-target-id="86" href="/" data-ph-href="/">
#           <ppc-content key="footer-newUniversalCompanyList1LinkText" data-ph-id="ph-page-element-footer-8onyzk-2pfCQY">
#            Careers
#           </ppc-content></a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-wkWIre"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="About Microsoft" key-href="footer-newUniversalCompanyList2LinkUrl" href="https://www.microsoft.com/en-us/about" target="_blank" key-target="footer-newUniversalCompanyList2TargetValue" aria-label="About Microsoft opens in a new tab" key-aria-label="footer-newUniversalCompanyList2LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-sUNOzb" role="link" class="au-target" au-target-id="87">
#           <ppc-content key="footer-newUniversalCompanyList2LinkText" data-ph-id="ph-page-element-footer-8onyzk-3S73n7">
#            About Microsoft
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-1oGKp9"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Company news" class="footer-click au-target" key-href="footer-newUniversalCompanyList3LinkUrl" href="https://news.microsoft.com/" target="_blank" key-target="footer-newUniversalCompanyList3TargetValue" aria-label="Company news opens in a new tab" key-aria-label="footer-newUniversalCompanyList3LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-Q5HUeP" role="link" au-target-id="88">
#           <ppc-content key="footer-newUniversalCompanyList3LinkText" data-ph-id="ph-page-element-footer-8onyzk-ZOm7H7">
#            Company news
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-WmFSqA"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Privacy at Microsoft" class="footer-click au-target" key-href="footer-newUniversalCompanyList4LinkUrl" href="https://privacy.microsoft.com/en-us" target="_blank" key-target="footer-newUniversalCompanyList4TargetValue" aria-label="Privacy at Microsoft opens in a new tab" key-aria-label="footer-newUniversalCompanyList4LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-K5rmQq" role="link" au-target-id="89">
#           <ppc-content key="footer-newUniversalCompanyList4LinkText" data-ph-id="ph-page-element-footer-8onyzk-AtRRgg">
#            Privacy at Microsoft
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-0ZI8Q4"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Investors" class="footer-click au-target" key-href="footer-newUniversalCompanyList5LinkUrl" href="https://www.microsoft.com/investor/default.aspx" target="_blank" key-target="footer-newUniversalCompanyList5TargetValue" aria-label="Investors opens in a new tab" key-aria-label="footer-newUniversalCompanyList5LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-tGkaeP" role="link" au-target-id="90">
#           <ppc-content key="footer-newUniversalCompanyList5LinkText" data-ph-id="ph-page-element-footer-8onyzk-4o75St">
#            Investors
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-bLumkV"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Diversity and inclusion" class="footer-click au-target" key-href="footer-newUniversalCompanyList6LinkUrl" href="https://www.microsoft.com/en-us/diversity/" target="_blank" key-target="footer-newUniversalCompanyList6TargetValue" aria-label="Diversity and inclusion opens in a new tab" key-aria-label="footer-newUniversalCompanyList6LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-ro1dpl" role="link" au-target-id="91">
#           <ppc-content key="footer-newUniversalCompanyList6LinkText" data-ph-id="ph-page-element-footer-8onyzk-C1ettF">
#            Diversity and inclusion
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-joc5Yo"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Accessibility" class="footer-click au-target" key-href="footer-newUniversalCompanyList7LinkUrl" href="https://www.microsoft.com/en-us/accessibility" target="_blank" key-target="footer-newUniversalCompanyList7TargetValue" aria-label="Accessibility opens in a new tab" key-aria-label="footer-newUniversalCompanyList7LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-hDKIRs" role="link" au-target-id="92">
#           <ppc-content key="footer-newUniversalCompanyList7LinkText" data-ph-id="ph-page-element-footer-8onyzk-QmgmP4">
#            Accessibility
#           </ppc-content> </a> </li>
#         <li data-ph-id="ph-page-element-footer-8onyzk-L9eOaZ"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Security" class="footer-click au-target" key-href="footer-newUniversalCompanyList8LinkUrl" href="https://www.microsoft.com/en-us/security/default.aspx" target="_blank" key-target="footer-newUniversalCompanyList8TargetValue" aria-label="Security opens in a new tab" key-aria-label="footer-newUniversalCompanyList8LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-CbeP1s" role="link" au-target-id="93">
#           <ppc-content key="footer-newUniversalCompanyList8LinkText" data-ph-id="ph-page-element-footer-8onyzk-dys1XI">
#            Security
#           </ppc-content> </a> </li>
#        </ul>
#       </div>
#      </div>
#      <div class="shell-footer-text" data-ph-id="ph-page-element-footer-8onyzk-sxT3tv">
#       <ul data-ph-id="ph-page-element-footer-8onyzk-UQQXdt">
#        <li data-ph-id="ph-page-element-footer-8onyzk-39l35z"> <p data-ph-id="ph-page-element-footer-8onyzk-Hhcasa">
#          <ppc-content key="footer-newUniversalHostedByPhenomParaText" data-ph-id="ph-page-element-footer-8onyzk-R3m0O7">
#           This site is hosted for Microsoft by Phenom People
#          </ppc-content> </p> </li>
#       </ul>
#      </div>
#      <div class="shell-footer-copyright" data-ph-id="ph-page-element-footer-8onyzk-8XvB6t">
#       <ul data-ph-id="ph-page-element-footer-8onyzk-1uhJRm">
#        <li data-ph-id="ph-page-element-footer-8onyzk-dg6QOZ"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Sitemap" class="ctl_footerNavLink au-target" key-href="footer-newUniversalHostedList1LinkUrl" href="https://www.microsoft.com/en-us/sitemap1.aspx" target="_blank" key-target="footer-newUniversalHostedList1TargetValue" aria-label="Sitemap opens in a new tab" key-aria-label="footer-newUniversalHostedList1LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-l52p50" role="link" au-target-id="94">
#          <ppc-content key="footer-newUniversalHostedList1LinkText" data-ph-id="ph-page-element-footer-8onyzk-gIlMXX">
#           Sitemap
#          </ppc-content> </a> </li>
#        <li data-ph-id="ph-page-element-footer-8onyzk-JODr3I"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Contact Microsoft" class="ctl_footerNavLink au-target" key-href="footer-newUniversalHostedList2LinkUrl" href="https://go.microsoft.com/fwlink/?LinkId=521839" target="_blank" key-target="footer-newUniversalHostedList2TargetValue" aria-label="Contact Microsoft opens in a new tab" key-aria-label="footer-newUniversalHostedList2LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-Z34nBb" role="link" au-target-id="95">
#          <ppc-content key="footer-newUniversalHostedList2LinkText" data-ph-id="ph-page-element-footer-8onyzk-QLPiYw">
#           Contact Microsoft
#          </ppc-content> </a> </li>
#        <li data-ph-id="ph-page-element-footer-8onyzk-44mqac"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Privacy &amp; cookies" class="ctl_footerNavLink au-target" key-href="footer-newUniversalHostedList3LinkUrl" href="https://go.microsoft.com/fwlink/?LinkId=521839" target="_blank" key-target="footer-newUniversalHostedList3TargetValue" aria-label="Privacy &amp; cookies opens in a new tab" key-aria-label="footer-newUniversalHostedList3LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-3zd0nI" role="link" au-target-id="96">
#          <ppc-content key="footer-newUniversalHostedList3LinkText" data-ph-id="ph-page-element-footer-8onyzk-YvZCjh">
#           Privacy &amp; cookies
#          </ppc-content> </a> </li>
#        <li data-ph-id="ph-page-element-footer-8onyzk-s0hLfQ"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Terms of use" class="ctl_footerNavLink au-target" key-href="footer-newUniversalHostedList4LinkUrl" href="https://go.microsoft.com/fwlink/?LinkID=206977" target="_blank" key-target="footer-newUniversalHostedList4TargetValue" aria-label="Terms of use opens in a new tab" key-aria-label="footer-newUniversalHostedList4LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-Ie6iYZ" role="link" au-target-id="97">
#          <ppc-content key="footer-newUniversalHostedList4LinkText" data-ph-id="ph-page-element-footer-8onyzk-VS4ezE">
#           Terms of use
#          </ppc-content> </a> </li>
#        <li data-ph-id="ph-page-element-footer-8onyzk-uZyToR"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Trademarks" class="ctl_footerNavLink au-target" key-href="footer-newUniversalHostedList5LinkUrl" href="https://www.microsoft.com/trademarks" target="_blank" key-target="footer-newUniversalHostedList5TargetValue" aria-label="Trademarks opens in a new tab" key-aria-label="footer-newUniversalHostedList5LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-uqMRTB" role="link" au-target-id="98">
#          <ppc-content key="footer-newUniversalHostedList5LinkText" data-ph-id="ph-page-element-footer-8onyzk-FQ8GTq">
#           Trademarks
#          </ppc-content> </a> </li>
#        <li data-ph-id="ph-page-element-footer-8onyzk-1oR6UW"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="Safety &amp; eco" class="ctl_footerNavLink au-target" key-href="footer-newUniversalHostedList6LinkUrl" href="https://www.microsoft.com/en-us/devices/safety-and-eco" target="_blank" key-target="footer-newUniversalHostedList6TargetValue" aria-label="Safety &amp; eco opens in a new tab" key-aria-label="footer-newUniversalHostedList6LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-uF56Wz" role="link" au-target-id="99">
#          <ppc-content key="footer-newUniversalHostedList6LinkText" data-ph-id="ph-page-element-footer-8onyzk-GPudeR">
#           Safety &amp; eco
#          </ppc-content> </a> </li>
#        <li data-ph-id="ph-page-element-footer-8onyzk-BWlDTL"> <a ph-tevent="footer_menu_click" data-ph-tevent-attr-trait62="About our ads" class="ctl_footerNavLink au-target" key-href="footer-newUniversalHostedList7LinkUrl" href="https://choice.microsoft.com" target="_blank" key-target="footer-newUniversalHostedList7TargetValue" aria-label="About our ads opens in a new tab" key-aria-label="footer-newUniversalHostedList7LinkLabelText" data-ph-id="ph-page-element-footer-8onyzk-Po98tm" role="link" au-target-id="100">
#          <ppc-content key="footer-newUniversalHostedList7LinkText" data-ph-id="ph-page-element-footer-8onyzk-UAgdIi">
#           About our ads
#          </ppc-content> </a> </li>
#        <li role="presentation" data-ph-id="ph-page-element-footer-8onyzk-NTuDgD">
#         <ppc-content key="footer-newUniversalHostedList8MsftCopyrightText" data-ph-id="ph-page-element-footer-8onyzk-pwqvTc">
#          © Microsoft 2019
#         </ppc-content> </li>
#       </ul>
#      </div>
#     </div>
#    </div>
#   </div>
#  </footer>
# </div></section></div>
#   <script type="text/javascript" src="https://prodcmscdn.azureedge.net/careerconnectresources/p/MICRUS/en_us/desktop/assets/scripts/1566567863453-custom.js?v=1" data-ph-id="ph-page-element-page19-yja8NJ"></script>
#   <!-- <script>
#             phApp.validationRules = {
#                 "createJobAlertModel": {
#                     "alertName": {
#                         "presence": {
#                             "message": "MSG_E101"
#                         },
#                         "length": {
#                             "maximum": 192,
#                             "message": "MSG_E102"
#                         }
#                     }
#                 }
#             }
#             phApp.messages = {
#                 "MSG_E101": "Alert name is required",
#                 "MSG_E102": "Alert name cannot exceed 192 characters"
#             }
#     </script> -->
#  <script type="text/javascript" src="https://prodcmscdn.azureedge.net/careerconnectresources/p/common/js/vendor/mutation-observer-1.1.js?v=1" data-main="aurelia-bootstrapper"> </script><script type="text/javascript" src="https://prodcmscdn.azureedge.net/careerconnectresources/p/common/js/vendor/vendor-bundle-1.5.js?v=1" data-main="aurelia-bootstrapper"> </script><script type="text/javascript" src="https://prodcmscdn.azureedge.net/careerconnectresources/p/common/js/common/ph-common-bundle-1.41.js?v=1"></script><script type="text/javascript" src="https://prodcmscdn.azureedge.net/careerconnectresources/p/MICRUS/page-scripts/ph-page-1566832076592.js?v=1"></script>
# <div id="csrfToken" style="display:none">ba3e9a1cbf8b4833a2d43c3dc7dc7425</div>
# <script type="text/javascript" id="">window.clickTaleTagInjected||!function(b,d,e){function c(){var a=b.createElementNS;a=a?a.call(b,"http://www.w3.org/1999/xhtml",d):b.createElement(d);var c=b.getElementsByTagName(d)[0];a.async=!0;a.crossOrigin="anonymous";a.type="text/javascript";a.src=e;c.parentNode.insertBefore(a,c)}clickTaleTagInjected=!0;"loading"!=b.readyState?c():b.addEventListener("DOMContentLoaded",function(){setTimeout(c,0)})}(document,"script","https://cdnssl.clicktale.net/www32/ptc/b61598e7-9c00-482d-8d71-56d726c2f593.js");</script><script type="text/javascript" id="" src="https://az725175.vo.msecnd.net/scripts/jsll-4.js"></script><script type="text/javascript" id="" src="https://cdn.optimizely.com/js/8196639338.js"></script>
# <script type="text/javascript" id="">var config={useDefaultContentName:!0,isLoggedIn:!0,syncMuid:!0,debounceMs:{scroll:600,resize:3E3},autoCapture:{scroll:!0,resize:!0,addin:!0,assets:!0},coreData:{appId:"Careersbeta",env:"prod",market:window.phApp.locale,pageName:window.document.title,pageType:window.phApp.pageName}};awa.init(config);</script><div id="ClickTaleDiv" style="display: none;"></div><script crossorigin="anonymous" src="https://cdnssl.clicktale.net/www/WR-latest.js" type="text/javascript" async=""></script><iframe src="https://a3698060313.cdn.optimizely.com/client_storage/a3698060313.html" hidden="" aria-hidden="true" tabindex="-1" title="Optimizely Internal Frame" height="0" width="0" style="display: none;"></iframe><style type="text/css">.aurelia-hide { display:none !important; }</style></body></html>
# """
#
#
# # print(len(data))
# x = requests.get("https://careers.microsoft.com/us/en/search-results?keywords=php", verify=False)
# x.encoding = 'utf-8'
# data = x.text
# # print(data)
# x = re.findall('<a(.*)>', data)
# for y in x:
#     t = re.findall(" href=\"(.*?)\"", y)
#     if t:
#         link = t[0]
#         if "careers" in link and "job" in link:
#             print(link)
