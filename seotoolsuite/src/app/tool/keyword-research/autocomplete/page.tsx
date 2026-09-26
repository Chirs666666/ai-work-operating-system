import { Metadata } from "next";
import KeywordAutocompleteToolClient from "./Client";

export const metadata: Metadata = {
  title: "Keyword Autocomplete (Free) | SEOToolSuite",
  description:
    "The Keyword Autocomplete tool generates long-tail keyword ideas using Google autocomplete data for free.",
  openGraph: {
    type: "website",
    title: "Keyword Autocomplete (Free) | SEOToolSuite",
    description:
      "The Keyword Autocomplete tool generates long-tail keyword ideas using Google autocomplete data for free.",
    images: [{ url: "/assets/images/keyword-autocomplete-screenshot.png" }],
  },
  robots: {
    index: false,
  },
};

export default async function KeywordAutocompletePage({
  searchParams,
}: {
  searchParams: Promise<{
    keyword?: string;
    location_code?: string;
    language_code?: string;
  }>;
}) {
  const searchParameters = await searchParams;

  return <KeywordAutocompleteToolClient searchParams={searchParameters} />;
}
