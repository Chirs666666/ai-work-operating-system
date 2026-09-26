import type { Metadata } from "next";
import HomeHeader from "@/components/HomeHeader";
import { HomeFooter } from "@/components/HomeFooter";
import CostCalculator from "./CostCalculator";

export const metadata: Metadata = {
  title: "Pricing | SEOToolSuite",
  description:
    "Discover the simple and transparent pricing of SEOToolSuite, based on credits. Stop overpaying for SEO tools every month.",
  openGraph: {
    type: "website",
    title: "Pricing | SEOToolSuite",
    description:
      "Discover the simple and transparent pricing of SEOToolSuite, based on credits. Stop overpaying for SEO tools every month.",
    images: [
      {
        url: "/assets/images/seotoolsuite-homepage-screenshot.png",
      },
    ],
  },
};

export default function PricingPage() {
  return (
    <div className="pricing-page relative flex w-full flex-col bg-white">
      <HomeHeader />
      <section className="hero w-full border-b-2 border-slate-200 bg-[url('/assets/images/papyrus.png')] bg-repeat px-4 lg:px-0">
        <div className="mx-auto flex w-full max-w-350 flex-col items-center pt-8 lg:pt-14">
          <h1 className="text-center text-3xl font-semibold text-sky-950 capitalize sm:text-4xl lg:text-6xl">
            Pricing
          </h1>
          <p className="mt-4 max-w-225 text-center text-base font-medium text-balance text-black/60 sm:text-lg lg:text-xl">
            Discover the <b className="font-semibold text-sky-950">simple</b>{" "}
            and <b className="font-semibold text-sky-950">transparent</b>{" "}
            pricing of SEOToolSuite, based on{" "}
            <b className="font-semibold text-sky-950">credits</b>. Pay only for{" "}
            <b className="font-semibold text-sky-950">DataForSEO API charges</b>
            , no{" "}
            <b className="font-semibold text-sky-950">
              extra or hidden charges
            </b>
            . Stop <b className="font-semibold text-sky-950">overpaying</b> for
            SEO tools <b className="font-semibold text-sky-950">every month</b>.
            Use the{" "}
            <b className="font-semibold text-sky-950">cost calculator</b> below
            to estimate your costs now.
          </p>
          <div className="cost-calculator-container mx-auto mt-8 w-full max-w-250 rounded-t-md border-t-2 border-r-2 border-l-2 border-slate-200 bg-white">
            <CostCalculator />
          </div>
        </div>
      </section>
      <HomeFooter />
    </div>
  );
}
