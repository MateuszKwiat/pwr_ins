create table Band (
	ID int primary key not null,
	BandName varchar(255) not null default '',
	Genre varchar(255) not null default '',
	Country varchar(255) not null default '',
	YearFormed int not null default 0
)


create table Albums (
	ID int primary key not null,
	AlbumTitle varchar(255) not null default '',
	ReleaseYear varchar(255) not null default '',
	BandID int not null
);

alter table Albums 
add foreign key (BandID) references Band(ID)


create table Members (
	ID int primary key not null,
	MemberName varchar(255) not null default '',
	Instrument varchar(255) not null default '',
	BandID int not null
);

alter table Members
add foreign key (BandID) references Band(ID)


create table Concerts (
	ID int primary key not null,
	Venue varchar(255) not null default '',
	Date date not null
)


create table ConcertBands (
	ConcertID int not null,
	BandID int not null
);

alter table ConcertBands
add foreign key (ConcertID) references Concerts(ID);

alter table ConcertBands
add foreign key (BandID) references Band(ID)


create type genre as enum('', 'Rock', 'Pop', 'Jazz', 'Blues', 'Hip Hop', 'Metal');

create table MusicGenres (
	ID int primary key not null,
	GenreName genre not null default ''
)