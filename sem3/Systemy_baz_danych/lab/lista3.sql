create table countryinfo (
	doc json,
	_id varchar(32) identity('a','a') not null,
	primary key (_id)
);
/*
create table country (
	Code char(3) primary key not null default 'UNK' check (char_length(Code) >= 3),
	Name varchar(255) not null default '',
	Code2 char(2) not null unique default ''
);


create table city (
	ID int primary key not null,
	Name varchar(255) not null default '',
	CountryCode char(3) not null default '',
	District varchar(255) not null default '',
	Info json default null
);

alter table country 
add column Capital int default null;

alter table country
add foreign key (Capital) references city(ID);


create type strBool as enum('T', 'F');

create table countryLanguage (
	CountryCode char(3) not null default '',
	Language char(30) not null default '',
	IsOfficial strBool not null default 'F',
	Percentage double precision not null default 0.0,
	primary key (CountryCode, Language)
);

alter table countryLanguage
add foreign key (CountryCode) references country(Code);

create index languageCountryCode on countryLanguage(CountryCode);
*/