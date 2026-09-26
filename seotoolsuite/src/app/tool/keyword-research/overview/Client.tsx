"use client";

import KeywordOverviewTool from "@/tools/KeywordResearch/KeywordOverview";

const KeywordOverviewToolClient = ({
  searchParams,
}: {
  searchParams: {
    keyword?: string;
    location_code?: string;
    language_code?: string;
  };
}) => {
  return (
    <div className="keyword-overview-tool-page">
      <KeywordOverviewTool searchParams={searchParams} />
    </div>
  );
};

export default KeywordOverviewToolClient;
