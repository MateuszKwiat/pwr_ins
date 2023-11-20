/*
insert into country values
(1, 'Armenia', 'Erywan', 2791000, 0.759, 13),
(2, 'Brazil', 'Brasilia', 214300000, 0.766, 1609),
(3, 'Switzerland', 'Bern', 8703000, 0.962, 8006),
(4, 'Czech Republic', 'Prague', 10510000, 0.897, 2818),
(5, 'Poland', 'Warsaw', 37750000, 0.876, 6794),
(6, 'Egypt', 'Kair', 109300000, 0.734, 4041),
(7, 'Denmark', 'Copenhagen', 5857000, 0.946, 3983),
(8, 'Finland', 'Helsinki', 5541000, 0.938, 2973),
(9, 'France', 'Paris', 67750000, 0.898, 2958),
(10, 'Croatia', 'Zagreb', 3899000, 0.861, 6896),
(11, 'Iran', 'Teheran', 87920000, 0.783, 3597),
(12, 'Greece', 'Athens', 10640000, 0.886, 2149),
(13, 'Norway', 'Oslo', 5408000, 0.961, 4822),
(14, 'Pakistan', 'Islamabad', 231400000, 0.546, 3483),
(15, 'Qatar', 'Doha', 2688000, 0.855, 1797),
(16, 'Sweden', 'Stockholm', 10420000, 0.947, 6357),
(17, 'Turkey', 'Ankara', 84780000, 0.838, 819),
(18, 'Ukraine', 'Kyiv', 43790000, 0.786, 2001),
(19, 'Taiwan', 'Taipei', 23570000, 0.926, 7907),
(20, 'Zimbabwe', 'Harare', 15990000, 0.593, 2837);

select * from country order by population;

select min(population) from country;
update country set population = 20000000 where population = 2688000;

select * from country where population < 20000000;

delete from country where population < 20000000;
select * from country;
*/