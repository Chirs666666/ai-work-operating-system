"use client";

import KeywordAutocompleteTool from "@/tools/KeywordResearch/KeywordAutocomplete";

const KeywordAutocompleteToolClient = ({
  searchParams,
}: {
  searchParams: {
    keyword?: string;
    location_code?: string;
    language_code?: string;
  };
}) => {
  return (
    <div className="keyword-autocomplete-tool-page">
      <KeywordAutocompleteTool searchParams={searchParams} />
    </div>
  );
};

export default KeywordAutocompleteToolClient;
