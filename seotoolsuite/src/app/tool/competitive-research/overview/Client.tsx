"use client";

import TrafficOverviewTool from "@/tools/CompetitiveResearch/TrafficOverview";

const TrafficOverviewToolClient = ({
  searchParams,
}: {
  searchParams: {
    target?: string;
    location_code?: string;
    language_code?: string;
  };
}) => {
  return (
    <div className="traffic-overview-tool-page">
      <TrafficOverviewTool searchParams={searchParams} />
    </div>
  );
};

export default TrafficOverviewToolClient;
