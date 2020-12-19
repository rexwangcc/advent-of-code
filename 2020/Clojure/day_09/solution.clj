(ns day_09.solution
  (:require [clojure.string :as str]
            [main :as main :refer [defoverload]]))

(def day "09")

(defn get-lines
  "Read in inputs as seq of integers."
  [file]
  (map read-string (str/split-lines (slurp file))))

(defn two-sum
  [inputs target]
  (loop [l  inputs
         seen #{}]
    (when-let [curr (first l)]
      (if (seen (- target curr))
        true
        (recur (rest l) (conj seen curr))))))

(defn slide
  "Slide through the list using a window and
   outsource the searching to 2sum."
  [inputs]
  (letfn [(get-preamble-window [coll n offset]
            (->> coll
                 (drop offset)
                 (take n)))]
    (loop [offset 0
           idx 25]
      (let [window (get-preamble-window inputs 25 offset)
            curr (nth inputs idx)]
        (if-not (two-sum window curr)
          ;; found the outlier
          curr
          ;; keep running
          (recur (inc offset)
                 (inc idx)))))))

(defn find-contiguous-set
  "Slide a window, expand on right and
   shrink at left to find the target."
  [inputs magical-number]
  (letfn [(sum-by-index [coll i j]
            (reduce + (subvec (vec coll) i j)))]
    (loop [left 0
           right 1]
      (let [sum (sum-by-index inputs left right)]
        (if (= sum magical-number)
          ;; add together the smallest and largest number in this contiguous range
          (let [window (subvec (vec inputs) left right)]
            (+ (apply min window)
               (apply max window)))
          ;; keep shrinking/expanding the window
          (if (< sum magical-number)
            (recur left (inc right))
            (recur (inc left) right)))))))

(defn part1
  [_]
  (let [inputs (get-lines "day_09/inputs.txt")]
    (slide inputs)))

(defn part2
  [_]
  (let [inputs (get-lines "day_09/inputs.txt")
        magical-number (->> inputs
                            slide)]
    (find-contiguous-set inputs magical-number)))

(defoverload main/part1 day part1)
(defoverload main/part2 day part2)
