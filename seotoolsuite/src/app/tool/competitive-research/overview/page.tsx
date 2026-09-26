import { Metadata } from "next";
import TrafficOverviewToolClient from "./Client";

export const metadata: Metadata = {
  title: "Traffic Overview | SEOToolSuite",
  description:
    "The Traffic Overview tool analyzes a website’s organic and paid search performance.",
  openGraph: {
    type: "website",
    title: "Traffic Overview | SEOToolSuite",
    description:
      "The Traffic Overview tool analyzes a website’s organic and paid search performance.",
    images: [{ url: "/assets/images/traffic-overview-screenshot.png" }],
  },
  robots: {
    index: false,
  },
};

export default async function TrafficOverviewPage({
  searchParams,
}: {
  searchParams: Promise<{
    target?: string;
    location_code?: string;
    language_code?: string;
  }>;
}) {
  const searchParameters = await searchParams;

  return <TrafficOverviewToolClient searchParams={searchParameters} />;
}
