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
-- Name: partner; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.partner (
    partnerid integer NOT NULL,
    name character varying(255) NOT NULL,
    integrationdetails character varying(1000),
    lastdatasenttimestamp timestamp with time zone
);


--
-- Name: price; Type: TABLE; Schema: public; Owner: -
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


--
-- Name: product; Type: TABLE; Schema: public; Owner: -
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


--
-- Name: productspecification; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.productspecification (
    productspecificationid integer NOT NULL,
    productid integer NOT NULL,
    specification character varying(1000) NOT NULL,
    specificationtimestamp timestamp with time zone NOT NULL
);


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
-- Name: productspecification productspecification_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.productspecification
    ADD CONSTRAINT productspecification_pkey PRIMARY KEY (productspecificationid);


--
-- Name: price price_productid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.price
    ADD CONSTRAINT price_productid_fkey FOREIGN KEY (productid) REFERENCES public.product(productid);


--
-- Name: product product_partnerid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_partnerid_fkey FOREIGN KEY (partnerid) REFERENCES public.partner(partnerid);


--
-- Name: productspecification productspecification_productid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.productspecification
    ADD CONSTRAINT productspecification_productid_fkey FOREIGN KEY (productid) REFERENCES public.product(productid);


--
-- PostgreSQL database dump complete
--

