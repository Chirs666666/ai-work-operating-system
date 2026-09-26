"use client";

import KeywordSuggestionsTool from "@/tools/KeywordResearch/KeywordSuggestions";

const KeywordSuggestionsToolClient = ({
  searchParams,
}: {
  searchParams: {
    keyword?: string;
    location_code?: string;
    language_code?: string;
  };
}) => {
  return (
    <div className="keyword-suggestions-tool-page">
      <KeywordSuggestionsTool searchParams={searchParams} />
    </div>
  );
};

export default KeywordSuggestionsToolClient;
