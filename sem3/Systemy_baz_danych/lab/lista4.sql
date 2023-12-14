select doc->'Name', doc->'GNP' from countryinfo
	where (doc->>'GNP')::float =
	(select max((doc->>'GNP')::float)
		from countryinfo)


select max((doc->>'GNP')::float), min((doc->>'GNP')::float), 
avg((doc->>'GNP')::float)
from countryinfo group by (doc->'geography'->'Continent')::text


select city.name, countryinfo.doc->'geography'->>'Continent' from city
left join countryinfo on countryinfo.doc->>'_id'=city.CountryCode
where countryinfo.doc->'geography'->>'Continent'='North America'
order by city.name