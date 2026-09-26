import { Metadata } from "next";
import BulkDRCheckerToolClient from "./Client";

export const metadata: Metadata = {
  title: "Bulk Ahrefs DR Checker (Free) | SEOToolSuite",
  description:
    "The Bulk DR Checker tool lets you check the Ahrefs Domain Rating (DR) of multiple domains in a single request. It's ideal for evaluating backlink prospects, analyzing competitors, and assessing domain authority at scale.",
  openGraph: {
    type: "website",
    title: "Bulk Ahrefs DR Checker (Free) | SEOToolSuite",
    description:
      "The Bulk DR Checker tool lets you check the Ahrefs Domain Rating (DR) of multiple domains in a single request. It's ideal for evaluating backlink prospects, analyzing competitors, and assessing domain authority at scale.",
    images: [{ url: "/assets/images/bulk-dr-checker-screenshot.png" }],
  },
  robots: {
    index: false,
  },
};

export default function BulkDRCheckerPage() {
  return <BulkDRCheckerToolClient />;
}
