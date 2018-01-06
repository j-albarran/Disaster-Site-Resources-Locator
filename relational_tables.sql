create table Account(aid serial primary key, afirst varchar(50), alast varchar(50), email varchar(50));
create table Phone(phone_id serial primary key, aid integer references Account(aid), phone char(10));
create table Credentials(username varchar(50) primary key, password varchar(50), aid integer references Account(aid));
create table Region(rname varchar(50) primary key);
create table City(cname varchar(50) primary key, rname varchar(50) references Region(rname));
create table Address(addId serial primary key, street varchar(50), number integer, unit varchar(50), zipcode char(5), aid integer references Account(aid), cname varchar(50) references City(cname));
create table Administrator(adminId integer primary key references Account(aid));
create table Supplier(sid integer primary key references Account(aid));
create table Requester(rid integer primary key references Account(aid));
create table Bank_Account(bid serial primary key, routing integer, accountNumber integer, BankName varchar(50), sid integer references Supplier(sid));
Create table Payment (payid serial primary key, rid int references Requester(rid));

create table Category(cat_name varchar(50) primary key, cat_pname varchar(50));
create table Keyword(kid serial primary key, keyword varchar(50));
create table Resource(rsid serial primary key, rsname varchar(50), rdescription varchar(50), r_changed_date date, rqty integer, rprice float, r_supply_date date, sid integer references Supplier(sid), cat_name varchar(50) references Category(cat_name));
create table ResourceHasKeyword(rsid integer references Resource(rsid), kid integer references Keyword(kid), primary key(rsid, kid));
create table Resource_Requested(rrid serial primary key, rrqty integer, rrdescription varchar(50), rr_request_date date, rr_changed_date date, rid integer references Requester(rid), cat_name varchar(50) references Category(cat_name));
create table ResourceRequestedHasKeyword(rrid integer references Resource_Requested(rrid), kid integer references Keyword(kid), primary key(rrid, kid));

Create table Order_Info (oid serial primary key, odate Date, oprice float, ostatus varchar(50), payid int references Payment(payid));
Create table Transaction (tid serial primary key, tprice float, tqty int, tdate Date, sid int references Supplier(sid), bid int references Bank_Account(bid), rsid int references Resource(rsid), rid int references Requester(rid), oid int references Order_Info(oid) );
Create table Cash(cashid int primary key references Payment(payid));
Create table Credit_Card (cid int primary key references Payment(payid), card_number int, security_code int, ccname varchar(50), exp_date Date, rid int references Requester(rid), addid int references Address(addid) );
