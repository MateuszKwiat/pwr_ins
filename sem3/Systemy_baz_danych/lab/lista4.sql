select doc->'Name', doc->'GNP' from countryinfo
	where (doc->>'GNP')::float =
	(select max((doc->>'GNP')::float)
		from countryinfo)


select max((doc->>'GNP')::float), min((doc->>'GNP')::float), 
avg((doc->>'GNP')::float)--, doc->'geography'->'Continent'
from countryinfo group by (doc->'geography'->'Continent')::text


