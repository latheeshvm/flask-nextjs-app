import "../styles/globals.css";
import type { AppProps } from "next/app";
import Header from "../components/header";
import Footer from "../components/footer";

export default function App({
  Component,
  pageProps: { session, ...pageProps },
}: AppProps) {
  return (
    <>
      <Header />
      <Component {...pageProps} />
      <Footer />
    </>
  );
}
