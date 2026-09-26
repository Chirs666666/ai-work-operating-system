import { Metadata } from "next";
import RankedKeywordsToolClient from "./Client";

export const metadata: Metadata = {
  title: "Ranked Keywords | SEOToolSuite",
  description:
    "The Ranked Keywords tool shows the keywords a domain or page ranks for in search results.",
  openGraph: {
    type: "website",
    title: "Ranked Keywords | SEOToolSuite",
    description:
      "The Ranked Keywords tool shows the keywords a domain or page ranks for in search results.",
    images: [{ url: "/assets/images/ranked-keywords-screenshot.png" }],
  },
  robots: {
    index: false,
  },
};

export default async function RankedKeywordsPage({
  searchParams,
}: {
  searchParams: Promise<{
    target?: string;
    location_code?: string;
    language_code?: string;
  }>;
}) {
  const searchParameters = await searchParams;

  return <RankedKeywordsToolClient searchParams={searchParameters} />;
}
