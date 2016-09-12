#!/bin/bash

echo "Content-type: text/html"
echo ""

echo "<html>"
echo "<head>"
echo "<link rel=\"styles\" href=\"styles.css\" type=\"text/css\">"
echo "<title>Our Wiegley cgi project</title>"
echo "<body>"
echo "Holla Mundo Donovan Rosas"
echo "<h1 class=\"styleclass\">Test</h1>"
echo "${QUERY_STRING}"
if [ -n "${QUERY_STRING}" ] ; then
		/usr/bin/curl -s ${QUERY_STRING}
fi

echo "</body>"
echo "</html>"
