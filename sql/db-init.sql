drop table if exists universe; 
create table worlds (
       wid int(11) not null auto_increment, 
       title varchar(100) not null, 
       initial_state text not null,
       primary key (wid)
);

drop table if exists worldstate;
create table worldstate ( 
       wid int(11) not null,
       k varchar(45) not null, 
       v varchar(45) not null,
       primary key (wid,k)
);

drop table if exists kripke;
create table kripke (
       edge_id int(11) not null, 
       source_id int(11) not null, 
       destination_id int(11) not null,
       primary key (edge_id)
);

drop table if exists edge;
create table edge (
       edge_id int(11) not null, 
       predicate varchar(100) not null default '',
       effect varchar(100) not null,
       primary key (edge_id)
);

drop table if exists place;
create table place ( 
       pid int(11) not null auto_increment, 
       wid int(11) not null,
       title varchar(100) not null,
       content text not null, 
       image varchar(100) not null default '',
       primary key (pid)
);