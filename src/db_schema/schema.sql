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
SELECT pg_catalog.set_config('search_path', 'public', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: feeds; Type: TABLE; Schema: public; Owner: rares
--

CREATE TABLE public.feeds (
    feedid integer NOT NULL,
    partnerid integer NOT NULL,
    feedurl character varying(255) NOT NULL,
    lastretrievedtimestamp timestamp with time zone,
    feedtype character varying(50),
    laststatus character varying(50)
);


ALTER TABLE public.feeds OWNER TO rares;

--
-- Name: partner; Type: TABLE; Schema: public; Owner: rares
--

CREATE TABLE public.partner (
    partnerid integer NOT NULL,
    name character varying(255) NOT NULL,
    integrationdetails character varying(1000),
    lastdatasenttimestamp timestamp with time zone
);


ALTER TABLE public.partner OWNER TO rares;

--
-- Name: price; Type: TABLE; Schema: public; Owner: rares
--

CREATE TABLE public.price (
    priceid integer NOT NULL,
    productid integer NOT NULL,
    originalprice numeric(10,2) NOT NULL,
    saleprice numeric(10,2),
    shippingprice numeric(10,2),
    pricetimestamp timestamp with time zone NOT NULL,
    pricedate date NOT NULL
);


ALTER TABLE public.price OWNER TO rares;

--
-- Name: pricetrendsummary; Type: TABLE; Schema: public; Owner: rares
--

CREATE TABLE public.pricetrendsummary (
    pricetrendsummaryid integer NOT NULL,
    productid integer NOT NULL,
    partnerid integer NOT NULL,
    averageoriginalprice numeric(10,2) NOT NULL,
    averagesaleprice numeric(10,2) NOT NULL,
    minprice numeric(10,2) NOT NULL,
    maxprice numeric(10,2) NOT NULL
);


ALTER TABLE public.pricetrendsummary OWNER TO rares;

--
-- Name: product; Type: TABLE; Schema: public; Owner: rares
--

CREATE TABLE public.product (
    productid integer NOT NULL,
    partnerid integer,
    ean character varying(13) NOT NULL,
    producttitle character varying(255) NOT NULL,
    producturl character varying(1000) NOT NULL,
    sellername character varying(255),
    lastscrapedtimestamp timestamp with time zone
);


ALTER TABLE public.product OWNER TO rares;

--
-- Name: productspecification; Type: TABLE; Schema: public; Owner: rares
--

CREATE TABLE public.productspecification (
    productspecificationid integer NOT NULL,
    productid integer NOT NULL,
    specification character varying(1000) NOT NULL,
    specificationtimestamp timestamp with time zone NOT NULL
);


ALTER TABLE public.productspecification OWNER TO rares;

--
-- Name: scrapeerrorlog; Type: TABLE; Schema: public; Owner: rares
--

CREATE TABLE public.scrapeerrorlog (
    scrapeerrorlogid integer NOT NULL,
    scrapesessionid character(10) NOT NULL,
    errormessage character varying(255) NOT NULL,
    errortimestamp timestamp with time zone NOT NULL,
    errortype character varying(50),
    errorseverity character varying(50)
);


ALTER TABLE public.scrapeerrorlog OWNER TO rares;

--
-- Name: scraperconfig; Type: TABLE; Schema: public; Owner: rares
--

CREATE TABLE public.scraperconfig (
    scraperconfigid integer NOT NULL,
    configsettings character varying(25) NOT NULL,
    country character varying(2) NOT NULL,
    lastupdatedtimestamp timestamp with time zone NOT NULL,
    version character varying(50)
);


ALTER TABLE public.scraperconfig OWNER TO rares;

--
-- Name: scrapesession; Type: TABLE; Schema: public; Owner: rares
--

CREATE TABLE public.scrapesession (
    scrapesessionid character(10) NOT NULL,
    scraperconfigid integer,
    starttime timestamp with time zone NOT NULL,
    endtime timestamp with time zone,
    status character varying(50) NOT NULL,
    numberofproductsscraped integer NOT NULL,
    sessionduration time without time zone
);


ALTER TABLE public.scrapesession OWNER TO rares;

--
-- Name: scrapesummary; Type: TABLE; Schema: public; Owner: rares
--

CREATE TABLE public.scrapesummary (
    scrapesummaryid integer NOT NULL,
    productid integer NOT NULL,
    partnerid integer NOT NULL,
    averageduration time without time zone NOT NULL,
    successrate numeric(5,2) NOT NULL,
    totalerrors integer NOT NULL
);


ALTER TABLE public.scrapesummary OWNER TO rares;

--
-- Data for Name: feeds; Type: TABLE DATA; Schema: public; Owner: rares
--

COPY public.feeds (feedid, partnerid, feedurl, lastretrievedtimestamp, feedtype, laststatus) FROM stdin;
\.


--
-- Data for Name: partner; Type: TABLE DATA; Schema: public; Owner: rares
--

COPY public.partner (partnerid, name, integrationdetails, lastdatasenttimestamp) FROM stdin;
\.


--
-- Data for Name: price; Type: TABLE DATA; Schema: public; Owner: rares
--

COPY public.price (priceid, productid, originalprice, saleprice, shippingprice, pricetimestamp, pricedate) FROM stdin;
\.


--
-- Data for Name: pricetrendsummary; Type: TABLE DATA; Schema: public; Owner: rares
--

COPY public.pricetrendsummary (pricetrendsummaryid, productid, partnerid, averageoriginalprice, averagesaleprice, minprice, maxprice) FROM stdin;
\.


--
-- Data for Name: product; Type: TABLE DATA; Schema: public; Owner: rares
--

COPY public.product (productid, partnerid, ean, producttitle, producturl, sellername, lastscrapedtimestamp) FROM stdin;
\.


--
-- Data for Name: productspecification; Type: TABLE DATA; Schema: public; Owner: rares
--

COPY public.productspecification (productspecificationid, productid, specification, specificationtimestamp) FROM stdin;
\.


--
-- Data for Name: scrapeerrorlog; Type: TABLE DATA; Schema: public; Owner: rares
--

COPY public.scrapeerrorlog (scrapeerrorlogid, scrapesessionid, errormessage, errortimestamp, errortype, errorseverity) FROM stdin;
\.


--
-- Data for Name: scraperconfig; Type: TABLE DATA; Schema: public; Owner: rares
--

COPY public.scraperconfig (scraperconfigid, configsettings, country, lastupdatedtimestamp, version) FROM stdin;
\.


--
-- Data for Name: scrapesession; Type: TABLE DATA; Schema: public; Owner: rares
--

COPY public.scrapesession (scrapesessionid, scraperconfigid, starttime, endtime, status, numberofproductsscraped, sessionduration) FROM stdin;
\.


--
-- Data for Name: scrapesummary; Type: TABLE DATA; Schema: public; Owner: rares
--

COPY public.scrapesummary (scrapesummaryid, productid, partnerid, averageduration, successrate, totalerrors) FROM stdin;
\.


--
-- Name: feeds feeds_pkey; Type: CONSTRAINT; Schema: public; Owner: rares
--

ALTER TABLE ONLY public.feeds
    ADD CONSTRAINT feeds_pkey PRIMARY KEY (feedid);


--
-- Name: partner partner_pkey; Type: CONSTRAINT; Schema: public; Owner: rares
--

ALTER TABLE ONLY public.partner
    ADD CONSTRAINT partner_pkey PRIMARY KEY (partnerid);


--
-- Name: price price_pkey; Type: CONSTRAINT; Schema: public; Owner: rares
--

ALTER TABLE ONLY public.price
    ADD CONSTRAINT price_pkey PRIMARY KEY (priceid);


--
-- Name: pricetrendsummary pricetrendsummary_pkey; Type: CONSTRAINT; Schema: public; Owner: rares
--

ALTER TABLE ONLY public.pricetrendsummary
    ADD CONSTRAINT pricetrendsummary_pkey PRIMARY KEY (pricetrendsummaryid);


--
-- Name: product product_pkey; Type: CONSTRAINT; Schema: public; Owner: rares
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey PRIMARY KEY (productid);


--
-- Name: productspecification productspecification_pkey; Type: CONSTRAINT; Schema: public; Owner: rares
--

ALTER TABLE ONLY public.productspecification
    ADD CONSTRAINT productspecification_pkey PRIMARY KEY (productspecificationid);


--
-- Name: scrapeerrorlog scrapeerrorlog_pkey; Type: CONSTRAINT; Schema: public; Owner: rares
--

ALTER TABLE ONLY public.scrapeerrorlog
    ADD CONSTRAINT scrapeerrorlog_pkey PRIMARY KEY (scrapeerrorlogid);


--
-- Name: scraperconfig scraperconfig_pkey; Type: CONSTRAINT; Schema: public; Owner: rares
--

ALTER TABLE ONLY public.scraperconfig
    ADD CONSTRAINT scraperconfig_pkey PRIMARY KEY (scraperconfigid);


--
-- Name: scrapesession scrapesession_pkey; Type: CONSTRAINT; Schema: public; Owner: rares
--

ALTER TABLE ONLY public.scrapesession
    ADD CONSTRAINT scrapesession_pkey PRIMARY KEY (scrapesessionid);


--
-- Name: scrapesummary scrapesummary_pkey; Type: CONSTRAINT; Schema: public; Owner: rares
--

ALTER TABLE ONLY public.scrapesummary
    ADD CONSTRAINT scrapesummary_pkey PRIMARY KEY (scrapesummaryid);


--
-- Name: feeds feeds_partnerid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: rares
--

ALTER TABLE ONLY public.feeds
    ADD CONSTRAINT feeds_partnerid_fkey FOREIGN KEY (partnerid) REFERENCES public.partner(partnerid);


--
-- Name: price price_productid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: rares
--

ALTER TABLE ONLY public.price
    ADD CONSTRAINT price_productid_fkey FOREIGN KEY (productid) REFERENCES public.product(productid);


--
-- Name: pricetrendsummary pricetrendsummary_partnerid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: rares
--

ALTER TABLE ONLY public.pricetrendsummary
    ADD CONSTRAINT pricetrendsummary_partnerid_fkey FOREIGN KEY (partnerid) REFERENCES public.partner(partnerid);


--
-- Name: pricetrendsummary pricetrendsummary_productid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: rares
--

ALTER TABLE ONLY public.pricetrendsummary
    ADD CONSTRAINT pricetrendsummary_productid_fkey FOREIGN KEY (productid) REFERENCES public.product(productid);


--
-- Name: product product_partnerid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: rares
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_partnerid_fkey FOREIGN KEY (partnerid) REFERENCES public.partner(partnerid);


--
-- Name: productspecification productspecification_productid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: rares
--

ALTER TABLE ONLY public.productspecification
    ADD CONSTRAINT productspecification_productid_fkey FOREIGN KEY (productid) REFERENCES public.product(productid);


--
-- Name: scrapeerrorlog scrapeerrorlog_scrapesessionid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: rares
--

ALTER TABLE ONLY public.scrapeerrorlog
    ADD CONSTRAINT scrapeerrorlog_scrapesessionid_fkey FOREIGN KEY (scrapesessionid) REFERENCES public.scrapesession(scrapesessionid);


--
-- Name: scrapesession scrapesession_scraperconfigid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: rares
--

ALTER TABLE ONLY public.scrapesession
    ADD CONSTRAINT scrapesession_scraperconfigid_fkey FOREIGN KEY (scraperconfigid) REFERENCES public.scraperconfig(scraperconfigid);


--
-- Name: scrapesummary scrapesummary_partnerid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: rares
--

ALTER TABLE ONLY public.scrapesummary
    ADD CONSTRAINT scrapesummary_partnerid_fkey FOREIGN KEY (partnerid) REFERENCES public.partner(partnerid);


--
-- Name: scrapesummary scrapesummary_productid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: rares
--

ALTER TABLE ONLY public.scrapesummary
    ADD CONSTRAINT scrapesummary_productid_fkey FOREIGN KEY (productid) REFERENCES public.product(productid);


--
-- PostgreSQL database dump complete
--

