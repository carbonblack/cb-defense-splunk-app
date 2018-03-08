curl -X GET \
             -H "Authorization: bearer $SPLUNK_TOKEN"  \
                      -H "Cache-Control: no-cache" \
                               -H "Content-Type: text/html" \
                                        --url "https://appinspect.splunk.com/v1/app/report/$REPORT_ID"

