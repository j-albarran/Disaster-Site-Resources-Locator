create table Resource(rsid serial primary key, rname varchar(10), rdescription varchar(80), r_changed_date date, rqty integer, rprice float, r_supply_date date, sid integer references Supplier(sid), cat_name varchar(10) references Category(cat_name));
create table ResourceHasKeyword(rsid integer references Resource(rsid), kid integer references Keyword(kid), primary key(rsid, kid));
create table Keyword(kid serial primary key, keyword varchar(10));
create table ResourceRequestedHasKeyword(rrid integer references Resource(rrid), kid integer references Keyword(kid), primary key(rrid, kid));
create table Resource_Requested(rrid serial primary key, rrqty integer, rrdescription varchar(80), rr_request_date date, rr_changed_date date, rid integer references Requester(rid), cat_name varchar(10) references Category(cat_name));
create table Category(cat_name varchar(10) primary key);
