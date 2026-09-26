import { Metadata } from "next";
import KeywordOverviewToolClient from "./Client";

export const metadata: Metadata = {
  title: "Keyword Overview | SEOToolSuite",
  description:
    "The Keyword Overview tool gives a quick snapshot of a keyword’s performance, including search volume, intent, CPC, competition, trends, and audience insights.",
  openGraph: {
    type: "website",
    title: "Keyword Overview | SEOToolSuite",
    description:
      "The Keyword Overview tool gives a quick snapshot of a keyword’s performance, including search volume, intent, CPC, competition, trends, and audience insights.",
    images: [
      {
        url: "/assets/images/keyword-overview-screenshot.png",
      },
    ],
  },
  robots: {
    index: false,
  },
};

export default async function KeywordOverviewPage({
  searchParams,
}: {
  searchParams: Promise<{
    keyword?: string;
    location_code?: string;
    language_code?: string;
  }>;
}) {
  const searchParameters = await searchParams;

  return <KeywordOverviewToolClient searchParams={searchParameters} />;
}
