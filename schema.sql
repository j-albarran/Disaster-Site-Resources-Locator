create table Account(aid serial primary key, afirst varchar(20), alast varchar(20), email varchar(30));
create table Phone(phone_id serial primary key, aid integer references Account(aid), phone char(10));
create table Credentials(username varchar(20) primary key, password varchar(20), aid integer references Account(aid));
create table Region(rname varchar(20) primary key);
create table City(cname varchar(20) primary key, rname varchar(20) references Region(rname));
create table Address(addId serial primary key, street varchar(40), number integer, unit varchar(40), zipcode char(5), aid integer references Account(aid), cname varchar(20) references City(cname));
create table Administrator(adminId integer primary key references Account(aid));
create table Supplier(sid integer primary key references Account(aid));
create table Requester(rid integer primary key references Account(aid));
create table Bank_Account(bid serial primary key, routing integer, accountNumber integer, BankName varchar(20), sid integer references Supplier(sid));
Create table Payment (payid serial primary key, rid int references Requester(rid));

create table Category(cat_name varchar(25) primary key, cat_pname varchar(25));
create table Keyword(kid serial primary key, keyword varchar(25));
create table Resource(rsid serial primary key, rname varchar(25), rdescription varchar(25), r_changed_date date, rqty integer, rprice float, r_supply_date date, sid integer references Supplier(sid), cat_name varchar(25) references Category(cat_name));
create table ResourceHasKeyword(rsid integer references Resource(rsid), kid integer references Keyword(kid), primary key(rsid, kid));
create table Resource_Requested(rrid serial primary key, rrqty integer, rrdescription varchar(25), rr_request_date date, rr_changed_date date, rid integer references Requester(rid), cat_name varchar(25) references Category(cat_name));
create table ResourceRequestedHasKeyword(rrid integer references Resource_Requested(rrid), kid integer references Keyword(kid), primary key(rrid, kid));


Create table Order_Info (oid serial primary key, odate Date, oprice float, ostatus varchar(25), payid int references Payment(payid));

Create table Transaction (tid serial primary key, tprice float, tqty int, tdate Date,
sid int references Supplier(sid), bid int references Bank_Account(bid), rsid int references Resource(rsid),
rid int references Requester(rid), oid int references Order_Info(oid)
);

Create table Cash(cashid int primary key references Payment(payid));

Create table Credit_Card (cid int primary key references Payment(payid), card_number int, security_code int, ccname varchar(25),
exp_date Date, rid int references Requester(rid), addid int references Address(addid)
);
