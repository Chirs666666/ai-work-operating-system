import { Metadata } from "next";
import KeywordSuggestionsToolClient from "./Client";

export const metadata: Metadata = {
  title: "Keyword Suggestions | SEOToolSuite",
  description:
    "The Keyword Suggestions tool generates a large list of relevant keyword ideas based on your seed keyword.",
  openGraph: {
    type: "website",
    title: "Keyword Suggestions | SEOToolSuite",
    description:
      "The Keyword Suggestions tool generates a large list of relevant keyword ideas based on your seed keyword.",
    images: [{ url: "/assets/images/keyword-suggestions-screenshot.png" }],
  },
  robots: {
    index: false,
  },
};

export default async function KeywordSuggestionsPage({
  searchParams,
}: {
  searchParams: Promise<{
    keyword?: string;
    location_code?: string;
    language_code?: string;
  }>;
}) {
  const searchParameters = await searchParams;

  return <KeywordSuggestionsToolClient searchParams={searchParameters} />;
}
