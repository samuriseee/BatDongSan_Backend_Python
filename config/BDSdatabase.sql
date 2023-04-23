create database BDS_python;
use BDS_python;

-- create table tinh_tp (
-- 	id nvarchar(255) primary key not null,
--     ten nvarchar(50)
-- );
-- create table quan_huyen (
-- 	id nvarchar(255) primary key not null,
--     ten nvarchar(50),
--     id_tinh_tp nvarchar(255) references tinh_tp(id)
-- );
-- create table phuong_xa (
-- 	id nvarchar(255) primary key not null,
--     ten nvarchar(50),
--     id_quan_huyen nvarchar(255) references quan_huyen(id)
-- );
-- create table dia_chi_cu_the (
-- 	id nvarchar(255) primary key not null,
--     ten nvarchar(50),
--     id_phuong_xa nvarchar(255) references phuong_xa(id)
-- );

create table loai_nha_dat_cho_thue(
	id nvarchar(255) primary key not null,
    ten MEDIUMTEXT,
    link LONGTEXT
);
create table loai_nha_dat_ban(
	id nvarchar(255) primary key not null,
    ten MEDIUMTEXT,
    link LONGTEXT
);
create table bat_dong_san (
	id nvarchar(255) primary key not null,
    tieu_de MEDIUMTEXT,
    dia_chi_cu_the nvarchar(255),
    gia nvarchar(30),
    dien_tich float,
    sdt varchar(10),
    so_phong_ngu int,
    mo_ta LONGTEXT,
    nguoi_dang varchar(20),
    anh LONGTEXT,
    id_loai_ban nvarchar(255) references loai_nha_dat_cho_thue(id),
    id_loai_thue nvarchar(255) references loai_nha_dat_ban(id)
);
insert into loai_nha_dat_cho_thue(id,ten,link) values ('123','nha dat cho thue','hehehe');
insert into loai_nha_dat_ban(id,ten,link) values ('123','nha dat ban','hehehe');
insert into bat_dong_san(id,tieu_de,dia_chi_cu_the,gia,dien_tich,sdt,so_phong_ngu,mo_ta,nguoi_dang,anh,id_loai_ban,id_loai_thue) values ('BDS-123','Bat dong san BD', '777 hehe', '30000000', 333.2, '0000000', 2,'nha dep nhat viet nam','kiet vip pro', '["https://","https://","https://"]','123', null)


-- insert into tinh_tp(id,ten) values ('1234','Da Nang');
-- insert into quan_huyen(id,ten,id_tinh_tp) values ('444','hai Chau','1234'), ('555','Son Tra','1234');
-- insert into phuong_xa(id,ten,id_quan_huyen) values ('66', 'Thuan Phuoc', '444'), ('77','Thanh Binh','444'),('88','Thach thang','555');
-- insert into dia_chi_cu_the(id,ten,id_phuong_xa) values ('777', '99 ly thai do', '66');






