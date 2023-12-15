-- 2
select doc->'Name', doc->'GNP' from countryinfo
	where (doc->>'GNP')::float =
	(select max((doc->>'GNP')::float)
		from countryinfo)

-- 3
select max((doc->>'GNP')::float), min((doc->>'GNP')::float), 
avg((doc->>'GNP')::float)
from countryinfo group by (doc->'geography'->'Continent')::text

-- 4
select city.name, countryinfo.doc->'geography'->>'Continent' from city
left join countryinfo on countryinfo.doc->>'_id'=city.CountryCode
where countryinfo.doc->'geography'->>'Continent'='North America'
order by city.name

-- 5
select doc->>'Name', doc->'government'->>'HeadOfState'
from countryinfo
where doc->'government'->>'HeadOfState' like '%Elisabeth%'

-- 6
select count(doc->'geography'->>'Continent'), doc->'geography'->>'Continent'
from countryinfo
group by doc->'geography'->>'Continent'

-- 7
select doc->>'Name', doc->'demographics'->>'LifeExpectancy'
from countryinfo
order by doc->'demographics'->>'LifeExpectancy' 

select doc->>'Name', doc->'demographics'->>'LifeExpectancy'
from countryinfo
where doc->'demographics'->>'LifeExpectancy' != 'null'
order by doc->'demographics'->>'LifeExpectancy' desc
limit 10