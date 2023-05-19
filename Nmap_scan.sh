#!/bin/bash

read -p "Wprowadz sciezke do pliku: " FILE_PATH_NAME

function check_host() {
	if [[ -n $IP_ADDRESS ]]
	then
		ping_cmd=$(nmap -sn $IP_ADDRESS | grep "Host is up" | cut -d '(' -f 1)
		echo '----------------'
		if [[ -z $ping_cmd ]]
		then	
			printf "$IP_ADDRESS jest nieaktywny\n"
		else
			printf "$IP_ADDRESS jest aktywny\n"
			dns_name
		fi
	fi
}

function dns_name() {
	dns_name=$(host $IP_ADDRESS)
	printf "$dns_name\n"
}

while read -r IP_ADDRESS || [[ -n "$IP_ADDRESS" ]]
do
	check_host
done < "$FILE_PATH_NAME"