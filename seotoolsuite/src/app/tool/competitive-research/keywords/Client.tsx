"use client";

import RankedKeywordsTool from "@/tools/CompetitiveResearch/RankedKeywords";

const RankedKeywordsToolClient = ({
  searchParams,
}: {
  searchParams: {
    target?: string;
    location_code?: string;
    language_code?: string;
  };
}) => {
  return (
    <div className="ranked-keywords-tool-page">
      <RankedKeywordsTool searchParams={searchParams} />
    </div>
  );
};

export default RankedKeywordsToolClient;
