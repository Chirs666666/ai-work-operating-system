import type { MetadataRoute } from "next";

export default function robots(): MetadataRoute.Robots {
  const baseUrl: string = "https://seotoolsuite.nitishkgupta.com";

  return {
    rules: {
      userAgent: "*",
      allow: "/",
    },
    sitemap: `${baseUrl}/sitemap.xml`,
  };
}
