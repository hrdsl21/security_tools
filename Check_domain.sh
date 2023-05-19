#! /bin/bash	

read -p "Podaj nazwe domeny ktora chcesz atakowac" DOMAIN_NAME

function check_domain(){
	
	results=$(host $SUB_DOMAIN | grep 'has address')
	
	if [[ -n $results ]]
	then 
		printf "Znaleziono subdomene:$SUB_DOMAIN\n"
	fi
}

for sub in $(cat sub_domens.txt)
do 	
	SUB_DOMAIN=$sub.$DOMAIN_NAME
	check_domain
done
