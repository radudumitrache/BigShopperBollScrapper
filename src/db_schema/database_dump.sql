--
-- PostgreSQL database dump
--

-- Dumped from database version 14.10 (Homebrew)
-- Dumped by pg_dump version 14.10 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: feeds; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.feeds (
    feedid integer NOT NULL,
    productid integer,
    feedurl character varying(255),
    lastretrievedtimestamp timestamp with time zone,
    feedtype character varying(50),
    laststatus character varying(50)
);


--
-- Name: partner; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.partner (
    partnerid integer NOT NULL,
    name character varying(255),
    integrationdetails json,
    lastdatasenttimestamp timestamp with time zone
);


--
-- Name: price; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.price (
    priceid integer NOT NULL,
    productid integer,
    originalprice numeric(10,2),
    saleprice numeric(10,2),
    shippingprice numeric(10,2),
    pricetimestamp timestamp with time zone,
    pricedate date
);


--
-- Name: product; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.product (
    productid integer NOT NULL,
    scraperconfigid integer,
    ean character varying(13),
    producttitle character varying(255),
    producturl character varying(1000),
    lastscrapedtimestamp timestamp with time zone
);


--
-- Name: productpartner; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.productpartner (
    productid integer NOT NULL,
    partnerid integer NOT NULL,
    integrationdetails json,
    lastdatasenttimestamp timestamp with time zone
);


--
-- Name: productspecification; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.productspecification (
    productspecificationid integer NOT NULL,
    productid integer,
    specificationtimestamp timestamp with time zone
);


--
-- Name: scraperconfig; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.scraperconfig (
    scraperconfigid integer NOT NULL,
    configsettings character varying(100),
    country character varying(2),
    lastupdatedtimestamp timestamp with time zone,
    version character varying(50)
);


--
-- Data for Name: feeds; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.feeds (feedid, productid, feedurl, lastretrievedtimestamp, feedtype, laststatus) FROM stdin;
\.


--
-- Data for Name: partner; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.partner (partnerid, name, integrationdetails, lastdatasenttimestamp) FROM stdin;
\.


--
-- Data for Name: price; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.price (priceid, productid, originalprice, saleprice, shippingprice, pricetimestamp, pricedate) FROM stdin;
\.


--
-- Data for Name: product; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.product (productid, scraperconfigid, ean, producttitle, producturl, lastscrapedtimestamp) FROM stdin;
\.


--
-- Data for Name: productpartner; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.productpartner (productid, partnerid, integrationdetails, lastdatasenttimestamp) FROM stdin;
\.


--
-- Data for Name: productspecification; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.productspecification (productspecificationid, productid, specificationtimestamp) FROM stdin;
\.


--
-- Data for Name: scraperconfig; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.scraperconfig (scraperconfigid, configsettings, country, lastupdatedtimestamp, version) FROM stdin;
\.


--
-- Name: feeds feeds_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.feeds
    ADD CONSTRAINT feeds_pkey PRIMARY KEY (feedid);


--
-- Name: partner partner_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.partner
    ADD CONSTRAINT partner_pkey PRIMARY KEY (partnerid);


--
-- Name: price price_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.price
    ADD CONSTRAINT price_pkey PRIMARY KEY (priceid);


--
-- Name: product product_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey PRIMARY KEY (productid);


--
-- Name: productpartner productpartner_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.productpartner
    ADD CONSTRAINT productpartner_pkey PRIMARY KEY (productid, partnerid);


--
-- Name: productspecification productspecification_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.productspecification
    ADD CONSTRAINT productspecification_pkey PRIMARY KEY (productspecificationid);


--
-- Name: scraperconfig scraperconfig_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.scraperconfig
    ADD CONSTRAINT scraperconfig_pkey PRIMARY KEY (scraperconfigid);


--
-- Name: feeds feeds_productid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.feeds
    ADD CONSTRAINT feeds_productid_fkey FOREIGN KEY (productid) REFERENCES public.product(productid);


--
-- Name: price price_productid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.price
    ADD CONSTRAINT price_productid_fkey FOREIGN KEY (productid) REFERENCES public.product(productid);


--
-- Name: product product_scraperconfigid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_scraperconfigid_fkey FOREIGN KEY (scraperconfigid) REFERENCES public.scraperconfig(scraperconfigid);


--
-- Name: productpartner productpartner_partnerid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.productpartner
    ADD CONSTRAINT productpartner_partnerid_fkey FOREIGN KEY (partnerid) REFERENCES public.partner(partnerid);


--
-- Name: productpartner productpartner_productid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.productpartner
    ADD CONSTRAINT productpartner_productid_fkey FOREIGN KEY (productid) REFERENCES public.product(productid);


--
-- Name: productspecification productspecification_productid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.productspecification
    ADD CONSTRAINT productspecification_productid_fkey FOREIGN KEY (productid) REFERENCES public.product(productid);


--
-- PostgreSQL database dump complete
--

