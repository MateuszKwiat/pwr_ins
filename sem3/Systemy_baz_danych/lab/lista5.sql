-- 1


-- 2
select count(doc->'geography'->>'Continent'), doc->'geography'->>'Continent'
from countryinfo
group by doc->'geography'->>'Continent'
order by count(doc->'geography'->>'Continent') desc
limit 1

-- 3
select doc->>'Name', doc->>'IndepYear' 
from countryinfo
where doc->>'IndepYear' != 'null'
order by cast(doc->>'IndepYear' as integer) desc

-- 4


-- 5


-- 6


