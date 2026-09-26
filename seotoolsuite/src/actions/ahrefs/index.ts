"use server";

import Ahrefs from "@/services/Ahrefs";

export async function getDomainRatingFree(target: string): Promise<number> {
  try {
    const AhrefsService = new Ahrefs();
    const domainRating = await AhrefsService.getDomainRatingFree(target);

    return domainRating;
  } catch (error) {
    throw error;
  }
}
